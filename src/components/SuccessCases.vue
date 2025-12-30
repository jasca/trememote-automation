<script setup>
</script>

<template>
    <section class="py-24 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-b from-background via-surface/30 to-background pointer-events-none">
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Casos de Éxito</h2>
                <p class="text-xl text-gray-400">Resultados reales impulsados por automatización inteligente.</p>
            </div>

            <div class="grid md:grid-cols-2 gap-12">
                <!-- Case 1: VentaPropIA -->
                <div
                    class="glass-card rounded-2xl overflow-hidden hover:border-primary/50 transition-all duration-500 group">
                    <div class="h-64 overflow-hidden relative">
                        <img src="/ventapropia-case.png" alt="VentaPropIA Dashboard"
                            class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-110 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-surface to-transparent"></div>
                    </div>
                    <div class="p-8">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-2xl font-bold text-white">VentaPropIA</h3>
                            <span
                                class="bg-primary/20 text-primary-light px-3 py-1 rounded-full text-xs font-semibold">Real
                                Estate</span>
                        </div>
                        <p class="text-gray-400 mb-6">
                            Plataforma integral para agentes inmobiliarios. Automatización de leads desde portales,
                            calificación con IA y CRM con gestión de propiedades.
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
                        <a href="https://ventapropia.com.ar" target="_blank"
                            class="text-primary-light hover:text-white font-medium inline-flex items-center transition-colors">
                            Ver Caso Completo <span class="ml-2">→</span>
                        </a>
                    </div>
                </div>

                <!-- Case 2: MLBotty -->
                <div
                    class="glass-card rounded-2xl overflow-hidden hover:border-primary/50 transition-all duration-500 group">
                    <div class="h-64 overflow-hidden relative flex">
                        <div class="w-[65%] h-full relative">
                            <img src="/mlbotty-workflow.png" alt="MLBotty Workflow"
                                class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 opacity-70 group-hover:opacity-100">
                            <div class="absolute inset-0 bg-gradient-to-t from-surface to-transparent"></div>
                        </div>
                        <div
                            class="w-[35%] h-full relative border-l border-white/5 bg-black/20 flex items-center justify-center overflow-hidden p-2">
                            <img src="/mlbotty-chat.png" alt="MLBotty Chat"
                                class="h-full object-contain transition-transform duration-700 group-hover:scale-110 opacity-70 group-hover:opacity-100">
                            <div
                                class="absolute inset-0 bg-gradient-to-t from-surface to-transparent pointer-events-none">
                            </div>
                        </div>
                    </div>
                    <div class="p-8">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-2xl font-bold text-white">MLBotty</h3>
                            <span
                                class="bg-primary/20 text-primary-light px-3 py-1 rounded-full text-xs font-semibold">E-commerce
                                IA</span>
                        </div>
                        <p class="text-gray-400 mb-6">
                            Chat inteligente en lenguaje natural para la búsqueda y consulta de productos vía WhatsApp.
                            Automatización total desde la consulta hasta la visualización del producto.
                        </p>
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div>
                                <span class="block text-2xl font-bold text-white">95%</span>
                                <span class="text-sm text-gray-500">Automatización</span>
                            </div>
                            <div>
                                <span class="block text-2xl font-bold text-white">
                                    < 4s</span>
                                        <span class="text-sm text-gray-500">Tiempo Respuesta</span>
                            </div>
                        </div>
                        <div class="text-primary-light font-mono text-sm">
                            Powered by TMT-Nexus & Gemini
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
