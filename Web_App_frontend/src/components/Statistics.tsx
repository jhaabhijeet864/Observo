
import React from 'react';

const Statistics = () => {
  const stats = [
    { value: '99.9%', label: 'Detection Accuracy', gradient: 'from-green-400 to-emerald-500' },
    { value: '<10ms', label: 'Processing Time', gradient: 'from-blue-400 to-cyan-500' },
    { value: '24/7', label: 'Uptime Monitoring', gradient: 'from-purple-400 to-pink-500' },
    { value: '100+', label: 'Object Categories', gradient: 'from-orange-400 to-red-500' },
    { value: '97%', label: 'Map Accuracy', gradient: 'from-cyan-400 to-blue-500' },
  ];

  return (
    <section className="py-20 bg-gradient-to-r from-slate-900 to-blue-900">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Mission Critical Performance
          </h2>
          <p className="text-xl text-slate-300">
            Proven results in the most demanding space environments
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-5 gap-8 max-w-7xl mx-auto">
          {stats.map((stat, index) => (
            <div 
              key={index}
              className="text-center group transform hover:scale-105 transition-all duration-300"
            >
              <div className="relative">
                <div className={`text-5xl md:text-6xl font-bold bg-gradient-to-r ${stat.gradient} bg-clip-text text-transparent mb-4 animate-fade-in`}>
                  {stat.value}
                </div>
                <div className={`h-1 w-16 bg-gradient-to-r ${stat.gradient} mx-auto rounded-full mb-4 group-hover:w-24 transition-all duration-300`}></div>
              </div>
              <p className="text-slate-300 font-medium text-lg">{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Statistics;
