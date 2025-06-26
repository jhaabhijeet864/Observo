
import React from 'react';
import { Satellite, Star } from 'lucide-react';
import { Button } from '@/components/ui/button';

const Hero = () => {
  return (
    <div className="relative min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 overflow-hidden">
      {/* Animated stars background */}
      <div className="absolute inset-0">
        {[...Array(50)].map((_, i) => (
          <Star 
            key={i}
            className="absolute text-white animate-pulse opacity-20"
            size={Math.random() * 3 + 1}
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${Math.random() * 2 + 2}s`
            }}
          />
        ))}
      </div>

      {/* Main content */}
      <div className="relative z-10 container mx-auto px-4 py-20 flex flex-col items-center justify-center min-h-screen text-center">
        {/* Logo and title */}
        <div className="mb-8 animate-fade-in">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Satellite className="text-cyan-400 animate-spin" size={48} style={{ animationDuration: '10s' }} />
            <h1 className="text-6xl md:text-8xl font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
              VISTA-S
            </h1>
          </div>
          <div className="h-1 w-32 bg-gradient-to-r from-cyan-400 to-blue-400 mx-auto rounded-full mb-6"></div>
          <p className="text-lg md:text-xl text-cyan-300 font-semibold tracking-wider mb-4">
            VISUAL INTERFACE SYSTEM FOR TARGET ASSESSMENT - SPACE
          </p>
        </div>

        {/* Subtitle */}
        <h2 className="text-2xl md:text-4xl font-semibold text-white mb-6 max-w-4xl leading-tight">
          Advanced Space Station Object Detection
        </h2>

        {/* Description */}
        <p className="text-xl text-slate-300 mb-12 max-w-3xl leading-relaxed">
          Deliver a high-accuracy object detection model with comprehensive documentation, 
          optimized for space station safety operations using cutting-edge AI technology 
          designed specifically for the unique challenges of space environments.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col md:flex-row gap-4">
          <Button 
            size="lg" 
            className="bg-cyan-500 hover:bg-cyan-400 text-black font-semibold px-8 py-4 text-lg transition-all duration-300 hover:scale-105"
          >
            Start Detection
          </Button>
          <Button 
            size="lg" 
            variant="outline"
            className="border-cyan-400 text-cyan-400 hover:bg-cyan-400 hover:text-black font-semibold px-8 py-4 text-lg transition-all duration-300 hover:scale-105"
          >
            View Documentation
          </Button>
        </div>

        {/* Floating elements */}
        <div className="absolute top-20 left-10 animate-bounce" style={{ animationDelay: '1s', animationDuration: '3s' }}>
          <div className="w-3 h-3 bg-cyan-400 rounded-full opacity-60"></div>
        </div>
        <div className="absolute bottom-32 right-16 animate-bounce" style={{ animationDelay: '2s', animationDuration: '4s' }}>
          <div className="w-2 h-2 bg-blue-400 rounded-full opacity-60"></div>
        </div>
      </div>

      {/* Bottom gradient */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-slate-900 to-transparent"></div>
    </div>
  );
};

export default Hero;
