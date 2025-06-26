
import React from 'react';
import { Card } from '@/components/ui/card';
import { Rocket, Monitor, Star, Satellite } from 'lucide-react';

const Features = () => {
  const features = [
    {
      icon: <Rocket className="text-cyan-400" size={48} />,
      title: 'Advanced AI Models',
      description: 'Trained on thousands of space station images with state-of-the-art deep learning algorithms'
    },
    {
      icon: <Monitor className="text-blue-400" size={48} />,
      title: 'Real-time Processing',
      description: 'Process images in milliseconds with our optimized inference pipeline'
    },
    {
      icon: <Star className="text-yellow-400" size={48} />,
      title: 'Mission Critical Accuracy',
      description: '99.9% detection accuracy for critical space operations and safety protocols'
    },
    {
      icon: <Satellite className="text-purple-400" size={48} />,
      title: 'Object Classification',
      description: 'Identify equipment, tools, hazards, and anomalies with detailed confidence scores'
    }
  ];

  return (
    <section className="py-20 bg-slate-800">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Advanced Capabilities
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Cutting-edge AI technology designed specifically for the unique challenges of space environments
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
          {features.map((feature, index) => (
            <Card 
              key={index}
              className="bg-slate-900 border-slate-700 p-6 hover:border-cyan-400/50 transition-all duration-300 group hover:scale-105"
            >
              <div className="text-center">
                <div className="mb-6 group-hover:scale-110 transition-transform duration-300">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-white mb-4">
                  {feature.title}
                </h3>
                <p className="text-slate-300 leading-relaxed">
                  {feature.description}
                </p>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
