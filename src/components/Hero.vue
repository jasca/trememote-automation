<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentSlide = ref(0)
const slideInterval = ref(null)

const slides = [
    {
        tag: "Lead Automation 2026",
        titleLine1: "Gestión de Leads",
        titleLine2: "Ultra Rápida",
        description: "Captura, califica y responde consultas de WhatsApp y redes sociales en segundos con IA. No pierdas más ventas por falta de respuesta inmediata.",
        ctaPrimary: "Agendar Consultoría",
        ctaSecondary: "Ver Planes",
        type: 'leads'
    },
    {
        tag: "Operations & Workflows",
        titleLine1: "Operaciones",
        titleLine2: "Auto-Gestionadas",
        description: "Transforma procesos manuales en flujos autónomos. Conecta tus herramientas favoritas y deja que la IA gestione las tareas repetitivas de tu equipo.",
        ctaPrimary: "Optimizar Ahora",
        ctaSecondary: "Procesos IA",
        type: 'operations'
    },
    {
        tag: "Analytics & Automation",
        titleLine1: "Reportes",
        titleLine2: "Inteligentes",
        description: "Visualiza el rendimiento de tu negocio con dashboards dinámicos y reportes automáticos enviados directo a tu Slack, Email o WhatsApp.",
        ctaPrimary: "Probar Demo",
        ctaSecondary: "Ver Dashboards",
        type: 'reports'
    }
]

const nextSlide = () =>
{
    currentSlide.value = (currentSlide.value + 1) % slides.length
}

const setSlide = (index) =>
{
    currentSlide.value = index
    resetInterval()
}

const resetInterval = () =>
{
    if (slideInterval.value) clearInterval(slideInterval.value)
    slideInterval.value = setInterval(nextSlide, 8000)
}

onMounted(() =>
{
    resetInterval()
})

onUnmounted(() =>
{
    if (slideInterval.value) clearInterval(slideInterval.value)
})
</script>

<template>
    <section class="relative overflow-hidden pt-20 pb-32 md:pt-32 md:pb-40 min-h-[90vh] flex items-center">
        <!-- Ambient Glow Background -->
        <div class="absolute inset-0 z-0 text-secondary">
            <div
                class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary-dark/20 via-background to-background pointer-events-none">
            </div>
            <div
                class="absolute top-1/4 right-0 w-[500px] h-[500px] bg-primary/10 rounded-full blur-[128px] pointer-events-none">
            </div>
            <div
                class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-accent/10 rounded-full blur-[128px] pointer-events-none">
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
            <div class="relative">
                <!-- Slides Container -->
                <div class="overflow-hidden">
                    <div class="flex transition-transform duration-700 ease-in-out"
                        :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
                        <!-- Slide Loop -->
                        <div v-for="(slide, index) in slides" :key="index" class="w-full flex-shrink-0">
                            <div class="grid lg:grid-cols-2 gap-16 items-center">
                                <!-- Content -->
                                <div :class="{ 'animate-fade-in': currentSlide === index }">
                                    <div
                                        class="inline-flex items-center px-4 py-2 rounded-full border border-primary/30 bg-primary/10 text-primary-light text-sm font-medium mb-8 backdrop-blur-sm">
                                        <span class="mr-2 relative flex h-2 w-2">
                                            <span
                                                class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary-light opacity-75"></span>
                                            <span
                                                class="relative inline-flex rounded-full h-2 w-2 bg-primary-light"></span>
                                        </span>
                                        {{ slide.tag }}
                                    </div>

                                    <h1 class="text-5xl md:text-7xl font-bold leading-tight mb-8 tracking-tight">
                                        <span
                                            class="bg-clip-text text-transparent bg-gradient-to-r from-primary-light via-primary to-accent">{{
                                                slide.titleLine1 }}</span><br />
                                        <span class="text-white">{{ slide.titleLine2 }}</span>
                                    </h1>

                                    <p
                                        class="text-lg md:text-xl text-gray-400 mb-10 max-w-lg leading-relaxed font-light">
                                        {{ slide.description }}
                                    </p>

                                    <div class="flex flex-col sm:flex-row gap-5">
                                        <a href="#booking-modal"
                                            class="text-center bg-primary hover:bg-primary-light text-white px-8 py-4 rounded-xl font-semibold text-lg shadow-[0_0_20px_rgba(20,125,127,0.4)] hover:shadow-[0_0_30px_rgba(20,125,127,0.6)] transition-all duration-300 transform hover:-translate-y-1">
                                            {{ slide.ctaPrimary }}
                                        </a>
                                        <a href="#products"
                                            class="text-center glass text-white px-8 py-4 rounded-xl font-medium text-lg hover:bg-white/5 transition-all duration-300 border border-white/10">
                                            {{ slide.ctaSecondary }}
                                        </a>
                                    </div>
                                </div>

                                <!-- Visual Representation -->
                                <div class="relative mt-16 lg:mt-0 perspective-1000 hidden md:block">
                                    <div
                                        class="relative rounded-2xl border border-white/10 bg-surface/50 backdrop-blur-xl shadow-2xl p-1 overflow-hidden group hover:border-primary/30 transition-colors duration-500">
                                        <!-- Top Bar -->
                                        <div
                                            class="h-10 bg-black/40 border-b border-white/5 flex items-center px-4 space-x-2">
                                            <div class="flex space-x-1.5">
                                                <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
                                                <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
                                                <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
                                            </div>
                                            <div class="ml-4 text-xs text-gray-500 font-mono">
                                                {{ (index === 0 ? 'Lead_Automation_Workflow.json' : index === 1 ?
                                                    'Operations_Sync.json' : 'Dashboard_Reporter.json') }}
                                            </div>
                                        </div>

                                        <!-- Canvas Area -->
                                        <div
                                            class="h-[400px] w-full bg-[#1c1c1c] relative overflow-hidden bg-grid-pattern">
                                            <div class="absolute inset-0 opacity-[0.03]"
                                                style="background-image: radial-gradient(#fff 1px, transparent 1px); background-size: 20px 20px;">
                                            </div>

                                            <svg
                                                class="absolute inset-0 w-full h-full z-0 pointer-events-none overflow-visible">
                                                <path d="M140 100 C 180 100, 180 200, 220 200" stroke="#555"
                                                    stroke-width="2" fill="none" class="animate-pulse-slow" />
                                                <path d="M360 200 C 400 200, 400 200, 440 200" stroke="#555"
                                                    stroke-width="2" fill="none" />
                                                <path d="M540 200 C 560 200, 560 120, 600 120" stroke="#555"
                                                    stroke-width="2" fill="none" />
                                                <path d="M540 200 C 560 200, 560 280, 600 280" stroke="#555"
                                                    stroke-width="2" fill="none" />
                                            </svg>

                                            <!-- Nodes per type -->
                                            <div v-if="slide.type === 'leads'">
                                                <div
                                                    class="absolute top-[80px] left-[40px] w-[100px] h-[60px] bg-[#2d2d2d] rounded-lg border border-orange-500/50 shadow-lg flex flex-col items-center justify-center hover:scale-105 transition-transform z-10">
                                                    <div class="w-full h-1 bg-orange-500 absolute top-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-xl">⚡</span>
                                                    <span
                                                        class="text-[10px] text-gray-300 mt-1 font-mono">Webhook</span>
                                                </div>
                                                <div
                                                    class="absolute top-[170px] left-[220px] w-[140px] h-[70px] bg-[#2d2d2d] rounded-lg border border-green-500/50 shadow-lg flex items-center p-3 gap-3 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-green-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <div
                                                        class="w-8 h-8 rounded bg-green-900/30 flex items-center justify-center text-green-500">
                                                        🤖</div>
                                                    <div class="flex flex-col">
                                                        <span class="text-xs font-bold text-gray-200">OpenAI</span>
                                                        <span class="text-[9px] text-gray-500">Classify Intent</span>
                                                    </div>
                                                </div>
                                                <div
                                                    class="absolute top-[175px] left-[440px] w-[100px] h-[50px] bg-[#2d2d2d] rounded-lg border border-blue-500/50 shadow-lg flex items-center justify-center gap-2 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-blue-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-blue-400 font-bold text-xs">IF</span>
                                                    <span class="text-[10px] text-gray-400">Hot Lead?</span>
                                                </div>
                                                <div
                                                    class="absolute top-[90px] left-[600px] w-[120px] h-[60px] bg-[#2d2d2d] rounded-lg border border-teal-500/50 shadow-lg flex items-center p-2 gap-2 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-teal-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-teal-400 text-lg">💬</span>
                                                    <span class="text-[10px] text-gray-300">WhatsApp API</span>
                                                </div>
                                            </div>

                                            <div v-if="slide.type === 'operations'">
                                                <div
                                                    class="absolute top-[80px] left-[40px] w-[100px] h-[60px] bg-[#2d2d2d] rounded-lg border border-blue-500/50 shadow-lg flex flex-col items-center justify-center hover:scale-105 transition-transform z-10">
                                                    <div class="w-full h-1 bg-blue-500 absolute top-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-xl">📅</span>
                                                    <span
                                                        class="text-[10px] text-gray-300 mt-1 font-mono">Calendar</span>
                                                </div>
                                                <div
                                                    class="absolute top-[170px] left-[220px] w-[140px] h-[70px] bg-[#2d2d2d] rounded-lg border border-purple-500/50 shadow-lg flex items-center p-3 gap-3 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-purple-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <div
                                                        class="w-8 h-8 rounded bg-purple-900/30 flex items-center justify-center text-purple-500">
                                                        🧠</div>
                                                    <div class="flex flex-col">
                                                        <span class="text-xs font-bold text-gray-200">OpenAI</span>
                                                        <span class="text-[9px] text-gray-500">Summary Task</span>
                                                    </div>
                                                </div>
                                                <div
                                                    class="absolute top-[175px] left-[440px] w-[100px] h-[50px] bg-[#2d2d2d] rounded-lg border border-pink-500/50 shadow-lg flex items-center justify-center gap-2 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-pink-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-pink-400 font-bold text-xs">#</span>
                                                    <span class="text-[10px] text-gray-400">Slack Notify</span>
                                                </div>
                                                <div
                                                    class="absolute top-[90px] left-[600px] w-[120px] h-[60px] bg-[#2d2d2d] rounded-lg border border-gray-400 shadow-lg flex items-center p-2 gap-2 hover:scale-105 transition-transform z-10">
                                                    <div class="w-full h-1 bg-white absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-white text-lg">📝</span>
                                                    <span class="text-[10px] text-gray-300">Notion Update</span>
                                                </div>
                                            </div>

                                            <div v-if="slide.type === 'reports'">
                                                <div
                                                    class="absolute top-[80px] left-[40px] w-[100px] h-[60px] bg-[#2d2d2d] rounded-lg border border-blue-400 shadow-lg flex flex-col items-center justify-center hover:scale-105 transition-transform z-10">
                                                    <div class="w-full h-1 bg-blue-400 absolute top-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-xl">🗄️</span>
                                                    <span class="text-[10px] text-gray-300 mt-1 font-mono">DB
                                                        Query</span>
                                                </div>
                                                <div
                                                    class="absolute top-[170px] left-[220px] w-[140px] h-[70px] bg-[#2d2d2d] rounded-lg border border-orange-400 shadow-lg flex items-center p-3 gap-3 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-orange-400 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <div
                                                        class="w-8 h-8 rounded bg-orange-900/30 flex items-center justify-center text-orange-400">
                                                        ⚙️</div>
                                                    <div class="flex flex-col">
                                                        <span class="text-xs font-bold text-gray-200">Process</span>
                                                        <span class="text-[9px] text-gray-500">Aggregate Data</span>
                                                    </div>
                                                </div>
                                                <div
                                                    class="absolute top-[175px] left-[440px] w-[100px] h-[50px] bg-[#2d2d2d] rounded-lg border border-green-600 shadow-lg flex items-center justify-center gap-2 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-green-600 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-green-400 font-bold text-xs">XLS</span>
                                                    <span class="text-[10px] text-gray-400">Sheet Export</span>
                                                </div>
                                                <div
                                                    class="absolute top-[90px] left-[600px] w-[120px] h-[60px] bg-[#2d2d2d] rounded-lg border border-red-500 shadow-lg flex items-center p-2 gap-2 hover:scale-105 transition-transform z-10">
                                                    <div
                                                        class="w-full h-1 bg-red-500 absolute top-0 left-0 rounded-t-lg">
                                                    </div>
                                                    <span class="text-red-400 text-lg">📧</span>
                                                    <span class="text-[10px] text-gray-300">Email Report</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Floating Badge -->
                                    <div
                                        class="absolute bottom-4 right-4 glass px-6 py-4 rounded-xl flex items-center gap-4 animate-float shadow-xl border border-white/10">
                                        <div
                                            class="w-12 h-12 rounded-full bg-green-500/20 flex items-center justify-center border border-green-500/40 shadow-[0_0_15px_rgba(34,197,94,0.2)]">
                                            <span class="text-green-400 font-bold text-xl">✓</span>
                                        </div>
                                        <div class="whitespace-nowrap">
                                            <p
                                                class="text-[10px] text-gray-400 uppercase tracking-[0.2em] font-medium mb-0.5">
                                                {{ (index === 0 ? 'Respuesta IA' : index === 1 ? 'Eficiencia' :
                                                    'Puntualidad') }}
                                            </p>
                                            <p class="text-white font-bold text-xl leading-none">
                                                {{ (index === 0 ? '+40 horas/mes' : index === 1 ? 'Error rate 0%' :
                                                    '100% On-time') }}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Carousel Controls -->
                <div class="absolute -bottom-12 left-0 right-0 flex justify-center gap-4 z-20">
                    <button v-for="(_, index) in slides" :key="index" @click="setSlide(index)" aria-label="ir al slide"
                        class="w-12 h-1.5 rounded-full transition-all duration-300"
                        :class="currentSlide === index ? 'bg-primary w-20' : 'bg-white/20 hover:bg-white/40'"></button>
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
    0% {
        stroke-opacity: 0.3;
        stroke-width: 1.5;
    }

    50% {
        stroke-opacity: 1;
        stroke-width: 2.5;
        stroke: #147d7f;
    }

    100% {
        stroke-opacity: 0.3;
        stroke-width: 1.5;
    }
}

.perspective-1000 {
    perspective: 1000px;
}

.animate-fade-in {
    animation: fadeIn 0.8s ease-out forwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.glass {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.bg-grid-pattern {
    background-image: radial-gradient(circle, #333 1px, transparent 1px);
    background-size: 30px 30px;
}
</style>
