import React from 'react';
import { Card } from '@/components/ui/card';
import { Circle, Monitor, Satellite, Star, Rocket } from 'lucide-react';

const Capabilities = () => {
  const capabilities = [
    {
      icon: <Circle className="text-green-400" size={32} />,
      title: 'Edge Computing',
      description: 'Run detection locally on space station hardware with minimal power consumption'
    },
    {
      icon: <Satellite className="text-blue-400" size={32} />,
      title: 'Space Optimized',
      description: 'Specifically designed for zero-gravity environments and space station conditions'
    },
    {
      icon: <Star className="text-red-400" size={32} />,
      title: 'Risk Assessment',
      description: 'Automatically categorize detected objects by safety risk levels'
    },
    {
      icon: <Monitor className="text-purple-400" size={32} />,
      title: 'Analytics Dashboard',
      description: 'Comprehensive reporting and trend analysis for space station operations'
    },
    {
      icon: <Circle className="text-cyan-400" size={32} />,
      title: '24/7 Monitoring',
      description: 'Continuous surveillance with automated alerts for critical situations'
    },
    {
      icon: <Rocket className="text-orange-400" size={32} />,
      title: 'Multi-Station Support',
      description: 'Compatible with ISS, commercial stations, and future space habitats'
    }
  ];

  return (
    <section className="py-20 bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Comprehensive Space Solutions
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Every feature designed with the demanding requirements of space operations in mind
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {capabilities.map((capability, index) => (
            <Card 
              key={index}
              className="bg-slate-800/50 border-slate-600 p-6 backdrop-blur-sm hover:bg-slate-800/70 transition-all duration-300 group"
            >
              <div className="flex items-start gap-4">
                <div className="group-hover:scale-110 transition-transform duration-300">
                  {capability.icon}
                </div>
                <div>
                  <h3 className="text-lg font-semibold text-white mb-3">
                    {capability.title}
                  </h3>
                  <p className="text-slate-300 leading-relaxed">
                    {capability.description}
                  </p>
                </div>
              </div>
            </Card>
          ))}
        </div>

        {/* Footer */}
        <div className="text-center mt-16 pt-16 border-t border-slate-700">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Satellite className="text-cyan-400" size={32} />
            <span className="text-2xl font-bold text-white">VISTA-S</span>
          </div>
          <p className="text-slate-400">
            Advanced Object Detection for Space Station Safety Operations
          </p>
        </div>
      </div>
    </section>
  );
};

export default Capabilities;
