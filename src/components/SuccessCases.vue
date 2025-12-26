<script setup>
</script>

<template>
  <section class="py-24 relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-b from-background via-surface/30 to-background pointer-events-none"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Casos de Éxito</h2>
        <p class="text-xl text-gray-400">Resultados reales impulsados por automatización inteligente.</p>
      </div>

      <div class="grid md:grid-cols-2 gap-12">
         <!-- Case 1: VentaPropIA -->
         <div class="glass-card rounded-2xl overflow-hidden hover:border-primary/50 transition-all duration-500 group">
             <div class="h-64 overflow-hidden relative">
                 <img src="/ventapropia-case.png" alt="VentaPropIA Dashboard" class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-110 opacity-80 group-hover:opacity-100">
                 <div class="absolute inset-0 bg-gradient-to-t from-surface to-transparent"></div>
             </div>
             <div class="p-8">
                 <div class="flex items-center justify-between mb-4">
                     <h3 class="text-2xl font-bold text-white">VentaPropIA</h3>
                     <span class="bg-primary/20 text-primary-light px-3 py-1 rounded-full text-xs font-semibold">Real Estate</span>
                 </div>
                 <p class="text-gray-400 mb-6">
                     Plataforma integral para agentes inmobiliarios. Automatización de leads desde portales, calificación con IA y CRM con gestión de propiedades.
                 </p>
                 <div class="grid grid-cols-2 gap-4 mb-6">
                     <div>
                         <span class="block text-2xl font-bold text-white">45%</span>
                         <span class="text-sm text-gray-500">Más Conversión</span>
                     </div>
                     <div>
                         <span class="block text-2xl font-bold text-white">20h</span>
                         <span class="text-sm text-gray-500">Ahorro Semanal</span>
                     </div>
                 </div>
                 <a href="https://ventapropia.com.ar" target="_blank" class="text-primary-light hover:text-white font-medium inline-flex items-center transition-colors">
                     Ver Caso Completo <span class="ml-2">→</span>
                 </a>
             </div>
         </div>

         <!-- Case 2: Placeholder -->
         <div class="glass-card rounded-2xl overflow-hidden border-2 border-dashed border-gray-700 hover:border-gray-500 transition-colors duration-300 flex flex-col justify-center items-center text-center p-12 min-h-[500px] opacity-70 hover:opacity-100">
             <div class="w-20 h-20 rounded-full bg-gray-800 flex items-center justify-center mb-6">
                 <span class="text-4xl">🚀</span>
             </div>
             <h3 class="text-2xl font-bold text-white mb-2">Tu Éxito Aquí</h3>
             <p class="text-gray-400 max-w-sm mx-auto mb-8">
                 Estamos listos para escribir el próximo caso de éxito contigo. Automatiza tus operaciones y escala tu negocio.
             </p>
             <a href="#contact" class="bg-white/10 hover:bg-white/20 text-white px-6 py-3 rounded-lg transition-colors font-medium">
                 Comenzar Proyecto
             </a>
         </div>
      </div>
    </div>
  </section>
</template>
