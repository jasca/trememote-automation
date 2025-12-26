<script setup>
</script>

<template>
  <section class="relative overflow-hidden pt-20 pb-32 md:pt-32 md:pb-40">
     <!-- Ambient Glow Background -->
     <div class="absolute inset-0 z-0">
          <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary-dark/20 via-background to-background pointer-events-none"></div>
          <div class="absolute top-1/4 right-0 w-[500px] h-[500px] bg-primary/10 rounded-full blur-[128px] pointer-events-none"></div>
          <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-accent/10 rounded-full blur-[128px] pointer-events-none"></div>
     </div>

     <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
           <!-- Content -->
           <div>
              <div class="inline-flex items-center px-4 py-2 rounded-full border border-primary/30 bg-primary/10 text-primary-light text-sm font-medium mb-8 backdrop-blur-sm animate-fade-in-up">
                <span class="mr-2 relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary-light opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-primary-light"></span>
                </span>
                Soluciones de Automatización 2026
              </div>
              
              <h1 class="text-5xl md:text-7xl font-bold leading-tight mb-8 tracking-tight">
                 <span class="bg-clip-text text-transparent bg-gradient-to-r from-primary-light via-primary to-accent">Automatización IA</span><br/>
                 <span class="text-white">y Optimización</span>
              </h1>
              
              <p class="text-lg md:text-xl text-gray-400 mb-10 max-w-lg leading-relaxed font-light">
                 De Excel a <strong>n8n</strong>. Transformamos procesos manuales en flujos de trabajo inteligentes, escalables y autónomos.
              </p>
              
              <div class="flex flex-col sm:flex-row gap-5">
                 <a href="#booking-modal" class="text-center bg-primary hover:bg-primary-light text-white px-8 py-4 rounded-xl font-semibold text-lg shadow-[0_0_20px_rgba(20,125,127,0.4)] hover:shadow-[0_0_30px_rgba(20,125,127,0.6)] transition-all duration-300 transform hover:-translate-y-1">
                    Agendar Consultoría
                 </a>
                 <a href="#products" class="text-center glass text-white px-8 py-4 rounded-xl font-medium text-lg hover:bg-white/5 transition-all duration-300 border border-white/10">
                    Ver Planes
                 </a>
              </div>
           </div>
           
           <!-- Visual Representation: Real n8n Nodes Mockup -->
           <div class="relative mt-16 lg:mt-0 perspective-1000">
               <!-- Card Geometry -->
               <div class="relative rounded-2xl border border-white/10 bg-surface/50 backdrop-blur-xl shadow-2xl p-1 overflow-hidden group hover:border-primary/30 transition-colors duration-500">
                   <!-- Top Bar -->
                   <div class="h-10 bg-black/40 border-b border-white/5 flex items-center px-4 space-x-2">
                       <div class="flex space-x-1.5">
                           <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
                           <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
                           <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
                       </div>
                       <div class="ml-4 text-xs text-gray-500 font-mono">Lead_Automation_Workflow.json</div>
                   </div>

                   <!-- Canvas Area -->
                   <div class="h-[400px] w-full bg-[#1c1c1c] relative overflow-hidden bg-grid-pattern">
                        <!-- Grid overlay (CSS pattern would go here, simulated with radial dots) -->
                        <div class="absolute inset-0 opacity-[0.03]" style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 20px 20px;"></div>

                        <!-- Connecting Lines (SVG) -->
                        <svg class="absolute inset-0 w-full h-full z-0 pointer-events-none overflow-visible">
                            <!-- Line 1: Trigger -> OpenAI -->
                            <path d="M140 100 C 180 100, 180 200, 220 200" stroke="#555" stroke-width="2" fill="none" class="animate-pulse-slow"/>
                            <!-- Line 2: OpenAI -> Switch -->
                            <path d="M360 200 C 400 200, 400 200, 440 200" stroke="#555" stroke-width="2" fill="none" />
                            <!-- Line 3: Switch -> WhatsApp (True) -->
                            <path d="M540 200 C 560 200, 560 120, 600 120" stroke="#555" stroke-width="2" fill="none" />
                            <!-- Line 4: Switch -> Sheets (False) -->
                            <path d="M540 200 C 560 200, 560 280, 600 280" stroke="#555" stroke-width="2" fill="none" />
                        </svg>

                        <!-- Node 1: Webhook Trigger -->
                        <div class="absolute top-[80px] left-[40px] w-[100px] h-[60px] bg-[#2d2d2d] rounded-lg border border-orange-500/50 shadow-lg flex flex-col items-center justify-center hover:scale-105 transition-transform cursor-pointer z-10 group/node">
                            <div class="w-full h-1 bg-orange-500 absolute top-0 rounded-t-lg"></div>
                            <span class="text-xl">⚡</span>
                            <span class="text-[10px] text-gray-300 mt-1 font-mono">Webhook</span>
                             <!-- Output Dot -->
                             <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-orange-500 rounded-full"></div>
                        </div>

                        <!-- Node 2: OpenAI -->
                        <div class="absolute top-[170px] left-[220px] w-[140px] h-[70px] bg-[#2d2d2d] rounded-lg border border-green-500/50 shadow-lg flex items-center p-3 gap-3 hover:scale-105 transition-transform cursor-pointer z-10">
                            <div class="w-full h-1 bg-green-500 absolute top-0 left-0 rounded-t-lg"></div>
                            <div class="w-8 h-8 rounded bg-green-900/30 flex items-center justify-center text-green-500">🤖</div>
                            <div class="flex flex-col">
                                <span class="text-xs font-bold text-gray-200">OpenAI</span>
                                <span class="text-[9px] text-gray-500">Classify Intent</span>
                            </div>
                            <!-- Input/Output Dots -->
                            <div class="absolute -left-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-gray-400 rounded-full"></div>
                            <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-green-500 rounded-full"></div>
                        </div>

                        <!-- Node 3: If / Switch -->
                        <div class="absolute top-[175px] left-[440px] w-[100px] h-[50px] bg-[#2d2d2d] rounded-lg border border-blue-500/50 shadow-lg flex items-center justify-center gap-2 hover:scale-105 transition-transform cursor-pointer z-10">
                            <div class="w-full h-1 bg-blue-500 absolute top-0 left-0 rounded-t-lg"></div>
                            <span class="text-blue-400 font-bold text-xs">IF</span>
                            <span class="text-[10px] text-gray-400">Hot Lead?</span>
                            <div class="absolute -left-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-gray-400 rounded-full"></div>
                            <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-blue-500 rounded-full"></div>
                        </div>

                        <!-- Node 4: WhatsApp -->
                        <div class="absolute top-[90px] left-[600px] w-[120px] h-[60px] bg-[#2d2d2d] rounded-lg border border-teal-500/50 shadow-lg flex items-center p-2 gap-2 hover:scale-105 transition-transform cursor-pointer z-10">
                            <div class="w-full h-1 bg-teal-500 absolute top-0 left-0 rounded-t-lg"></div>
                            <span class="text-teal-400 text-lg">💬</span>
                            <span class="text-[10px] text-gray-300">WhatsApp API</span>
                            <div class="absolute -left-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-gray-400 rounded-full"></div>
                        </div>

                        <!-- Node 5: Sheets -->
                        <div class="absolute top-[250px] left-[600px] w-[120px] h-[60px] bg-[#2d2d2d] rounded-lg border border-green-700/50 shadow-lg flex items-center p-2 gap-2 hover:scale-105 transition-transform cursor-pointer z-10">
                            <div class="w-full h-1 bg-green-700 absolute top-0 left-0 rounded-t-lg"></div>
                            <span class="text-green-600 text-lg">📊</span>
                            <span class="text-[10px] text-gray-300">Google Sheets</span>
                            <div class="absolute -left-1.5 top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-gray-400 rounded-full"></div>
                        </div>
                   </div>
               </div>
               
               <!-- Floating Badge -->
               <div class="absolute -bottom-6 -right-6 glass px-6 py-4 rounded-xl flex items-center gap-3 animate-float shadow-xl">
                    <div class="w-10 h-10 rounded-full bg-green-500/20 flex items-center justify-center border border-green-500/40">
                        <span class="text-green-400 font-bold">✓</span>
                    </div>
                    <div>
                        <p class="text-xs text-gray-400 uppercase tracking-wider">Costo Ahorrado</p>
                        <p class="text-white font-bold text-lg">$2,400/mes</p>
                    </div>
               </div>
           </div>
        </div>
     </div>
  </section>
</template>

<style scoped>
.animate-pulse-slow {
  animation: pulse-path 3s infinite ease-in-out;
}
@keyframes pulse-path {
  0% { stroke-opacity: 0.3; stroke-width: 1.5; }
  50% { stroke-opacity: 1; stroke-width: 2.5; stroke: #147d7f; }
  100% { stroke-opacity: 0.3; stroke-width: 1.5; }
}

.perspective-1000 {
  perspective: 1000px;
}
</style>
