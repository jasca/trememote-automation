<script setup>
</script>

<template>
  <section id="products" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Planes de Implementación</h2>
        <p class="text-xl text-secondary max-w-2xl mx-auto">Soluciones escalables montadas en infraestructura privada. Sin costos ocultos por ejecución.</p>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        <!-- Starter Plan -->
        <div class="glass-card p-8 rounded-2xl flex flex-col border border-white/5 hover:border-primary/50 transition-all duration-300 hover:-translate-y-2 group">
          <div class="mb-4">
            <span class="bg-primary/20 text-primary-light px-3 py-1 rounded-full text-sm font-semibold border border-primary/20">Inicial</span>
          </div>
          <h3 class="text-2xl font-bold mb-4 text-white">Emprendedor</h3>
          <p class="text-gray-400 mb-6">Ideal para comenzar a automatizar tareas administrativas y de marketing.</p>
          <ul class="space-y-4 mb-8 flex-1 text-gray-300">
            <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Hasta <strong>5 Workflows</strong> activos</span></li>
            <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>VPS Privado (Datos 100% tuyos)</span></li>
            <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Setup Inicial Incluido</span></li>
            <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Soporte por Email</span></li>
          </ul>
          <a href="#contact" class="block w-full text-center border-2 border-primary text-primary-light hover:bg-primary hover:text-white font-semibold py-3 rounded-lg transition-colors">
            Solicitar Cotización
          </a>
        </div>

        <!-- Business Plan (Featured) -->
        <div class="glass-card p-8 rounded-2xl flex flex-col border-2 border-primary relative transform md:-translate-y-4 shadow-[0_0_30px_rgba(20,125,127,0.2)]">
          <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gradient-to-r from-primary to-primary-dark text-white px-4 py-1 rounded-full text-sm font-semibold shadow-lg shadow-primary/50">Más Popular</div>
          <div class="mb-4 mt-2">
             <span class="bg-primary/20 text-primary-light px-3 py-1 rounded-full text-sm font-semibold border border-primary/20">Empresas</span>
          </div>
          <h3 class="text-2xl font-bold mb-4 text-white">Corporativo</h3>
          <p class="text-gray-400 mb-6">Para PyMEs que buscan optimizar operaciones complejas.</p>
          <ul class="space-y-4 mb-8 flex-1 text-gray-300">
             <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Hasta <strong>20 Workflows</strong> activos</span></li>
             <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>VPS Dedicado Optimizado</span></li>
             <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Integración con CRM/ERP</span></li>
             <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Dashboards de Métricas</span></li>
             <li class="flex items-start"><span class="text-primary-light mr-2 flex-shrink-0">✔</span> <span>Soporte Prioritario WhatsApp</span></li>
          </ul>
          <a href="#contact" class="block w-full text-center bg-gradient-to-r from-primary to-primary-dark hover:from-primary-light hover:to-primary text-white font-semibold py-3 rounded-lg shadow-lg hover:shadow-primary/50 transition-all duration-300">
            Solicitar Cotización
          </a>
        </div>

        <!-- White Label Plan -->
        <div class="glass-card p-8 rounded-2xl flex flex-col border border-white/5 hover:border-white/20 transition-all duration-300 hover:-translate-y-2 group">
          <div class="mb-4">
             <span class="bg-white/10 text-gray-300 px-3 py-1 rounded-full text-sm font-semibold border border-white/10">Partners</span>
          </div>
          <h3 class="text-2xl font-bold mb-4 text-white">Marca Blanca</h3>
          <p class="text-gray-400 mb-6">Solución integral para agencias o grandes volúmenes de datos.</p>
          <ul class="space-y-4 mb-8 flex-1 text-gray-300">
             <li class="flex items-start"><span class="text-white mr-2 flex-shrink-0">✔</span> <span>Workflows <strong>Ilimitados</strong></span></li>
             <li class="flex items-start"><span class="text-white mr-2 flex-shrink-0">✔</span> <span>VPS High-Performance Dedicado</span></li>
             <li class="flex items-start"><span class="text-white mr-2 flex-shrink-0">✔</span> <span>Branding Personalizado</span></li>
             <li class="flex items-start"><span class="text-white mr-2 flex-shrink-0">✔</span> <span>Consultoría Estratégica Trimestral</span></li>
             <li class="flex items-start"><span class="text-white mr-2 flex-shrink-0">✔</span> <span>SLA y Contrato de Confidencialidad</span></li>
          </ul>
          <a href="#contact" class="block w-full text-center bg-white/10 hover:bg-white/20 text-white font-semibold py-3 rounded-lg transition-colors border border-white/10">
            Contactar Ventas
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
