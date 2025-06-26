
import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Monitor, Circle } from 'lucide-react';

const DetectionDemo = () => {
  const [isDetecting, setIsDetecting] = useState(false);
  const [showResults, setShowResults] = useState(false);

  const handleStartDetection = () => {
    setIsDetecting(true);
    setTimeout(() => {
      setIsDetecting(false);
      setShowResults(true);
    }, 3000);
  };

  const detectionResults = [
    { object: 'Space Helmet', confidence: 99.8, risk: 'Low', color: 'text-green-400' },
    { object: 'Loose Tool', confidence: 97.3, risk: 'High', color: 'text-red-400' },
    { object: 'Communication Device', confidence: 95.1, risk: 'Low', color: 'text-green-400' },
    { object: 'Debris Fragment', confidence: 89.7, risk: 'Critical', color: 'text-red-500' },
  ];

  return (
    <section className="py-20 bg-slate-800">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Real-Time Detection System
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Experience our advanced AI detection capabilities in action
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-12 max-w-6xl mx-auto">
          {/* Detection Interface */}
          <Card className="bg-slate-900 border-slate-700 p-8">
            <div className="text-center">
              <Monitor className="text-cyan-400 mx-auto mb-6" size={64} />
              <h3 className="text-2xl font-semibold text-white mb-6">Detection Interface</h3>
              
              {/* Mock camera view */}
              <div className="bg-slate-800 rounded-lg p-6 mb-6 min-h-[200px] flex items-center justify-center relative overflow-hidden">
                {isDetecting && (
                  <div className="absolute inset-0 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 animate-pulse"></div>
                )}
                <div className="text-slate-400 text-center">
                  {isDetecting ? (
                    <div className="animate-spin">
                      <Circle size={48} className="text-cyan-400" />
                    </div>
                  ) : (
                    <div>
                      <p className="text-lg mb-2">Space Station Camera Feed</p>
                      <p className="text-sm opacity-60">Ready for detection</p>
                    </div>
                  )}
                </div>
              </div>

              <Button 
                onClick={handleStartDetection}
                disabled={isDetecting}
                className="bg-cyan-500 hover:bg-cyan-400 text-black font-semibold px-8 py-3 w-full transition-all duration-300"
              >
                {isDetecting ? 'Detecting...' : 'Start Detection'}
              </Button>
            </div>
          </Card>

          {/* Results Panel */}
          <Card className="bg-slate-900 border-slate-700 p-8">
            <h3 className="text-2xl font-semibold text-white mb-6 text-center">Detection Results</h3>
            
            {showResults ? (
              <div className="space-y-4">
                {detectionResults.map((result, index) => (
                  <div 
                    key={index}
                    className="bg-slate-800 rounded-lg p-4 border border-slate-700 animate-fade-in"
                    style={{ animationDelay: `${index * 0.2}s` }}
                  >
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-white font-medium">{result.object}</span>
                      <span className={`text-sm font-semibold ${result.color}`}>
                        {result.risk}
                      </span>
                    </div>
                    <div className="flex justify-between items-center">
                      <span className="text-slate-400 text-sm">Confidence:</span>
                      <span className="text-cyan-400 font-mono">{result.confidence}%</span>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center text-slate-400 py-12">
                <Circle className="mx-auto mb-4 opacity-50" size={48} />
                <p>Run detection to see results</p>
              </div>
            )}
          </Card>
        </div>
      </div>
    </section>
  );
};

export default DetectionDemo;
