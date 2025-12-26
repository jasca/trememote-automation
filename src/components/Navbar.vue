<script setup>
import { ref } from 'vue';

const isOpen = ref(false);
</script>

<template>
  <nav class="fixed w-full z-50 transition-all duration-300 backdrop-blur-md bg-black/20 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-20 items-center">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          <a href="#" class="flex items-center gap-2">
            <img src="/logo2.png" alt="Trememote Logo" class="h-14 w-auto" />
          </a>
        </div>

        <!-- Desktop Menu -->
        <div class="hidden md:flex items-center space-x-8">
          <a href="#services"
            class="text-gray-300 hover:text-white font-medium transition text-sm uppercase tracking-wider">Servicios</a>
          <a href="#products"
            class="text-gray-300 hover:text-white font-medium transition text-sm uppercase tracking-wider">Planes</a>
          <a href="#workflow"
            class="text-gray-300 hover:text-white font-medium transition text-sm uppercase tracking-wider">Automatización</a>

          <a href="#booking-modal"
            class="bg-primary hover:bg-primary-light text-white px-6 py-2 rounded-full font-semibold transition shadow-[0_0_15px_rgba(20,125,127,0.5)] hover:shadow-[0_0_25px_rgba(20,125,127,0.7)] transform hover:-translate-y-0.5">
            Agendar Entrevista
          </a>
        </div>

        <!-- Mobile Button -->
        <div class="md:hidden flex items-center">
          <button @click="isOpen = !isOpen" class="text-gray-700 hover:text-primary focus:outline-none">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isOpen"
      class="md:hidden pb-4 bg-black/90 backdrop-blur-xl border-t border-white/10 absolute top-20 left-0 w-full shadow-2xl">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <a href="#services"
          class="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-white/10">Servicios</a>
        <a href="#products"
          class="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-white/10">Planes</a>
        <a href="#workflow"
          class="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-white/10">Automatización</a>
        <a href="#booking-modal"
          class="block w-full text-center mt-4 bg-primary text-white px-5 py-3 rounded-md font-semibold hover:bg-primary-light shadow-lg">
          Agendar Entrevista
        </a>
      </div>
    </div>
  </nav>
</template>
