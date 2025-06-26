
import React from 'react';
import Hero from '@/components/Hero';
import Features from '@/components/Features';
import Statistics from '@/components/Statistics';
import Capabilities from '@/components/Capabilities';
import DetectionDemo from '@/components/DetectionDemo';

const Index = () => {
  return (
    <div className="min-h-screen bg-slate-900">
      <Hero />
      <DetectionDemo />
      <Statistics />
      <Features />
      <Capabilities />
    </div>
  );
};

export default Index;
