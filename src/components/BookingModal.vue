<script setup>
import { ref, onMounted, computed } from 'vue';

const isOpen = ref(false);
const loading = ref(false);
const availableSlots = ref([]);
const selectedDate = ref(null);
const selectedTime = ref(null);
const step = ref(1); // 1: Select Date, 2: Select Time, 3: Form, 4: Success, 5: Error

// Mocked availability (In production this would come from VITE_WEBHOOK_AVAILABILITY)
// We will try to fetch real availability if env var exists, otherwise mock
const fetchAvailability = async () => {
    loading.value = true;
    try {
        const webhookUrl = import.meta.env.VITE_WEBHOOK_AVAILABILITY;
        // Simulating fetch for now as the endpoint might not be live yet
        // const response = await fetch(webhookUrl);
        // const data = await response.json();
        
        // Mock data generator for next 7 days
        const dates = [];
        const today = new Date();
        for(let i=1; i<=7; i++) {
            const d = new Date(today);
            d.setDate(today.getDate() + i);
            if(d.getDay() !== 0 && d.getDay() !== 6) { // Skip weekends
                dates.push({
                    date: d.toISOString().split('T')[0],
                    display: d.toLocaleDateString('es-AR', { weekday: 'short', day: 'numeric', month: 'short' }),
                    slots: ['10:00', '11:00', '14:00', '15:30', '17:00']
                });
            }
        }
        availableSlots.value = dates;
    } catch (e) {
        console.error("Error fetching availability", e);
    } finally {
        loading.value = false;
    }
};

const openModal = () => {
    const hash = window.location.hash;
    if (hash === '#booking-modal') {
        isOpen.value = true;
        fetchAvailability();
        // Clear hash without scroll
        history.pushState("", document.title, window.location.pathname + window.location.search);
    }
};

// Listen for hash change to trigger modal
onMounted(() => {
    window.addEventListener('hashchange', openModal);
    // Check on load
    if(window.location.hash === '#booking-modal') {
        openModal();
    }
});

const selectDate = (date) => {
    selectedDate.value = date;
    step.value = 2;
};

const selectTime = (time) => {
    selectedTime.value = time;
    step.value = 3;
};

const formData = ref({
    name: '',
    email: '',
    company: '',
    notes: ''
});

const submitBooking = async () => {
    loading.value = true;
    try {
        const webhookBooking = import.meta.env.VITE_WEBHOOK_BOOKING;
        
        const payload = {
            ...formData.value,
            date: selectedDate.value.date,
            time: selectedTime.value
        };

        // Simulate API call
        console.log("Sending to Webhook:", webhookBooking, payload);
        await new Promise(r => setTimeout(r, 1500)); 
        
        // Real implementation:
        // await fetch(webhookBooking, {
        //    method: 'POST',
        //    headers: {'Content-Type': 'application/json'},
        //    body: JSON.stringify(payload)
        // });

        step.value = 4;
    } catch (e) {
        step.value = 5;
    } finally {
        loading.value = false;
    }
};

const closeModal = () => {
    isOpen.value = false;
    // Reset state after transition
    setTimeout(() => {
        step.value = 1;
        selectedDate.value = null;
        selectedTime.value = null;
        formData.value = { name: '', email: '', company: '', notes: '' };
    }, 300);
};
</script>

<template>
  <Teleport to="body">
      <div v-if="isOpen" class="fixed inset-0 z-[9999] flex items-center justify-center p-4">
          <!-- Backdrop -->
          <div class="absolute inset-0 bg-black/80 backdrop-blur-sm" @click="closeModal"></div>
          
          <!-- Modal Content -->
          <div class="glass-card w-full max-w-2xl rounded-2xl relative z-10 overflow-hidden shadow-2xl animate-fade-in-up border border-white/10 text-white min-h-[500px] flex flex-col bg-[#111827]">
              <!-- Header -->
              <div class="p-6 border-b border-white/10 flex justify-between items-center bg-white/5">
                  <div>
                      <h3 class="text-xl font-bold text-white">Agendar Entrevista</h3>
                      <p class="text-xs text-gray-400">Consultoría Gratuita de 30min</p>
                  </div>
                  <button @click="closeModal" class="text-gray-400 hover:text-white hover:bg-white/10 rounded-full p-2 transition">
                      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                  </button>
              </div>

              <div class="flex-1 p-6 overflow-y-auto relative">
                  
                  <!-- Loading Overlay -->
                  <div v-if="loading" class="absolute inset-0 bg-black/80 flex items-center justify-center z-20">
                      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-light"></div>
                  </div>

                  <!-- Step 1: Date Selection -->
                  <div v-if="step === 1">
                      <h4 class="text-lg font-medium mb-4 text-center">Selecciona un día</h4>
                      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                          <button v-for="day in availableSlots" :key="day.date" 
                              @click="selectDate(day)"
                              class="p-4 rounded-xl border border-white/10 bg-white/5 hover:bg-primary/20 hover:border-primary/50 transition flex flex-col items-center gap-1 group">
                              <span class="text-xs text-gray-400 uppercase group-hover:text-primary-light">{{ day.display.split(' ')[0] }}</span>
                              <span class="text-xl font-bold">{{ day.display.split(' ')[1] }}</span>
                          </button>
                      </div>
                  </div>

                  <!-- Step 2: Time Selection -->
                  <div v-else-if="step === 2">
                      <div class="flex items-center gap-2 mb-6">
                          <button @click="step = 1" class="text-sm text-gray-400 hover:text-white">← Volver</button>
                          <span class="text-gray-600">|</span>
                          <span class="text-primary-light font-medium">{{ selectedDate.display }}</span>
                      </div>
                      <h4 class="text-lg font-medium mb-4 text-center">Selecciona una hora</h4>
                      <div class="grid grid-cols-3 sm:grid-cols-5 gap-3">
                          <button v-for="slot in selectedDate.slots" :key="slot" 
                              @click="selectTime(slot)"
                              class="py-3 px-4 rounded-lg border border-white/10 bg-white/5 hover:bg-primary/20 hover:border-primary/50 text-center transition font-mono text-sm">
                              {{ slot }}
                          </button>
                      </div>
                  </div>

                  <!-- Step 3: Form -->
                  <div v-else-if="step === 3">
                       <div class="flex items-center gap-2 mb-6 text-sm">
                          <button @click="step = 2" class="text-gray-400 hover:text-white">← Cambiar Hora</button>
                          <span class="text-gray-600">|</span>
                          <span class="text-gray-300">{{ selectedDate.display }} - {{ selectedTime }}</span>
                      </div>
                      
                      <form @submit.prevent="submitBooking" class="space-y-4">
                          <div>
                              <label class="block text-sm font-medium text-gray-400 mb-1">Nombre Completo</label>
                              <input v-model="formData.name" type="text" required class="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:border-primary-light focus:ring-1 focus:ring-primary-light transition text-white placeholder-gray-500" placeholder="Tu nombre">
                          </div>
                          <div>
                              <label class="block text-sm font-medium text-gray-400 mb-1">Email Corporativo</label>
                              <input v-model="formData.email" type="email" required class="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:border-primary-light focus:ring-1 focus:ring-primary-light transition text-white placeholder-gray-500" placeholder="nombre@empresa.com">
                          </div>
                          <div>
                              <label class="block text-sm font-medium text-gray-400 mb-1">Empresa</label>
                              <input v-model="formData.company" type="text" class="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:border-primary-light focus:ring-1 focus:ring-primary-light transition text-white placeholder-gray-500" placeholder="Nombre de tu empresa">
                          </div>
                          <div>
                              <label class="block text-sm font-medium text-gray-400 mb-1">¿Qué proceso te gustaría automatizar?</label>
                              <textarea v-model="formData.notes" rows="3" class="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:border-primary-light focus:ring-1 focus:ring-primary-light transition text-white placeholder-gray-500"></textarea>
                          </div>
                          
                          <button type="submit" class="w-full bg-primary hover:bg-primary-light text-white font-bold py-4 rounded-xl shadow-lg shadow-primary/20 transition transform hover:-translate-y-0.5">
                              Confirmar Reunión
                          </button>
                      </form>
                  </div>

                  <!-- Step 4: Success -->
                  <div v-else-if="step === 4" class="flex flex-col items-center justify-center h-full text-center py-8">
                      <div class="w-20 h-20 bg-green-500/20 rounded-full flex items-center justify-center mb-6">
                          <svg class="w-10 h-10 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                      </div>
                      <h3 class="text-2xl font-bold text-white mb-2">¡Reunión Agendada!</h3>
                      <p class="text-gray-400 mb-8 max-w-xs mx-auto">Te hemos enviado un correo de confirmación con el link de la videollamada.</p>
                      <button @click="closeModal" class="bg-white/10 hover:bg-white/20 text-white px-8 py-3 rounded-lg transition">Cerrar</button>
                  </div>

                   <!-- Step 5: Error -->
                  <div v-else-if="step === 5" class="flex flex-col items-center justify-center h-full text-center py-8">
                      <div class="w-20 h-20 bg-red-500/20 rounded-full flex items-center justify-center mb-6">
                          <span class="text-4xl">⚠️</span>
                      </div>
                      <h3 class="text-2xl font-bold text-white mb-2">Hubo un error</h3>
                      <p class="text-gray-400 mb-8 max-w-xs mx-auto">No pudimos procesar tu solicitud. Por favor intenta nuevamente.</p>
                      <button @click="step = 3" class="text-primary-light hover:text-white underline">Volver a intentar</button>
                  </div>

              </div>
          </div>
      </div>
  </Teleport>
</template>

<style scoped>
.animate-fade-in-up {
  animation: fadeInUp 0.3s ease-out;
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
