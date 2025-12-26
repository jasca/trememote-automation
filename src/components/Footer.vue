<script setup>
</script>

<template>
  <footer id="contact" class="bg-black/50 border-t border-white/5 backdrop-blur-lg pt-16 pb-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid md:grid-cols-4 gap-12 mb-12">
        <div class="col-span-1 md:col-span-2">
           <span class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500 mb-6 block">Trememote</span>
           <p class="text-gray-400 max-w-sm mb-6 leading-relaxed">
             Socios estratégicos en la transformación digital de tu negocio.<br>
             Especialistas en n8n, AI y optimización de procesos.
           </p>
           <div class="flex space-x-4">
               <!-- Social Icons Placeholder -->
               <a href="#" class="text-gray-400 hover:text-primary-light transition"><span class="sr-only">LinkedIn</span>in</a>
               <a href="#" class="text-gray-400 hover:text-primary-light transition"><span class="sr-only">Twitter</span>X</a>
           </div>
        </div>
        
        <div>
           <h4 class="text-lg font-semibold mb-6 text-white">Explorar</h4>
           <ul class="space-y-3">
             <li><a href="#services" class="text-gray-400 hover:text-primary-light transition">Servicios</a></li>
             <li><a href="#products" class="text-gray-400 hover:text-primary-light transition">Planes</a></li>
             <li><a href="#workflow" class="text-gray-400 hover:text-primary-light transition">Automatización</a></li>
           </ul>
        </div>

        <div>
           <h4 class="text-lg font-semibold mb-6 text-white">Contacto</h4>
           <ul class="space-y-4">
             <li class="flex items-center text-gray-400 group">
               <span class="mr-3 text-xl group-hover:text-primary-light transition">📧</span> 
               <a href="mailto:comercial@trememote.com.ar" class="hover:text-white transition">comercial@trememote.com.ar</a>
             </li>
             <li class="flex items-center text-gray-400 group">
                <span class="mr-3 text-xl group-hover:text-primary-light transition">📱</span> 
                <span>+54 9 11 2338 3837</span>
             </li>
             <li class="pt-2">
                <a href="#booking-modal" class="inline-block bg-primary hover:bg-primary-light text-white px-6 py-3 rounded-lg transition shadow-lg hover:shadow-primary/30">
                  Agendar Entrevista
                </a>
             </li>
           </ul>
        </div>
      </div>
      
      <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
        <div class="mb-4 md:mb-0">
            &copy; {{ new Date().getFullYear() }} Trememote. Todos los derechos reservados.
        </div>
        <div class="flex space-x-6">
            <a href="#" class="hover:text-white transition">Privacidad</a>
            <a href="#" class="hover:text-white transition">Términos</a>
        </div>
      </div>
    </div>
  </footer>
</template>
