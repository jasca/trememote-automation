<script setup>
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Services from './components/Services.vue'
import Products from './components/Products.vue'
import Footer from './components/Footer.vue'
import SuccessCases from './components/SuccessCases.vue'
import BookingModal from './components/BookingModal.vue'
</script>

<template>
  <div class="min-h-screen font-sans text-secondary bg-background selection:bg-primary selection:text-white scroll-smooth">
    <Navbar />
    <main>
      <Hero />
      <Services />
      
      <!-- Section Breaker / Workflow Highlight -->
      <section id="workflow" class="py-20 relative overflow-hidden">
          <div class="absolute inset-0 bg-primary/5"></div>
          <div class="absolute inset-0 opacity-20 bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
          <div class="max-w-7xl mx-auto px-4 text-center relative z-10">
              <span class="text-primary-light font-bold tracking-widest uppercase mb-4 block animate-pulse">Automatización Sin Límites</span>
              <h2 class="text-3xl md:text-5xl font-bold mb-8 text-white">Conecta tus Apps Favoritas</h2>
              <div class="flex flex-wrap justify-center gap-10 opacity-70 grayscale hover:grayscale-0 transition-all duration-500">
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#0F9D58] transition-colors">Google Sheets</span>
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#25D366] transition-colors">WhatsApp</span>
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#4A154B] transition-colors">Slack</span>
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#EA4335] transition-colors">Gmail</span>
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#FF7A59] transition-colors">HubSpot</span>
                  <span class="text-2xl font-bold text-gray-300 hover:text-[#96BF48] transition-colors">Shopify</span>
              </div>
          </div>
      </section>

      <SuccessCases />
      <Products />
    </main>
    <Footer />
    <BookingModal />
  </div>
</template>

<style>
/* Global scroll behavior is handled by tailwind class 'scroll-smooth' if configured, else fallback */
html {
  scroll-behavior: smooth;
}
</style>
