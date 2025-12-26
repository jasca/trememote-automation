<script setup>
</script>

<template>
  <section id="services" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-20">
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Nuestros Servicios</h2>
        <p class="text-xl text-secondary max-w-2xl mx-auto">Acompañamiento integral para construir el futuro de tu empresa.</p>
      </div>

      <div class="grid md:grid-cols-2 gap-8">
         <!-- Consulting -->
         <div class="glass-card p-8 rounded-2xl flex flex-col sm:flex-row gap-6 hover:border-primary/50 transition duration-300 group">
             <div class="flex-shrink-0">
                 <div class="w-16 h-16 bg-primary/20 rounded-2xl flex items-center justify-center text-primary-light text-3xl group-hover:scale-110 transition-transform">
                     🧠
                 </div>
             </div>
             <div>
                 <h3 class="text-2xl font-bold mb-3 text-white group-hover:text-primary-light transition-colors">Consultoría Estratégica</h3>
                 <p class="text-gray-400 leading-relaxed mb-4">
                    Antes de automatizar, optimizamos. Realizamos un análisis profundo de tus operaciones para diseñar la arquitectura ideal.
                 </p>
                 <ul class="space-y-2 text-gray-300">
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> Diagramación de Flujos de Trabajo</li>
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> Plan de Acción Trimestral</li>
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> Documentación de Procesos</li>
                 </ul>
             </div>
         </div>

         <!-- VPS Hosting -->
         <div class="glass-card p-8 rounded-2xl flex flex-col sm:flex-row gap-6 hover:border-primary/50 transition duration-300 group">
             <div class="flex-shrink-0">
                 <div class="w-16 h-16 bg-primary/20 rounded-2xl flex items-center justify-center text-primary-light text-3xl group-hover:scale-110 transition-transform">
                     🔒
                 </div>
             </div>
             <div>
                 <h3 class="text-2xl font-bold mb-3 text-white group-hover:text-primary-light transition-colors">Infraestructura Dedicada (VPS)</h3>
                 <p class="text-gray-400 leading-relaxed mb-4">
                     Olvídate de plataformas compartidas. Implementamos tu propio servidor privado para control total y seguridad.
                 </p>
                 <ul class="space-y-2 text-gray-300">
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> Privacidad Absoluta de Datos</li>
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> Sin límites de ejecución</li>
                     <li class="flex items-center"><span class="text-primary mr-2">●</span> IPs Dedicadas y SSL Propio</li>
                 </ul>
             </div>
         </div>
      </div>
    </div>
  </section>
</template>
