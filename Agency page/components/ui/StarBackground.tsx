
import React, { useEffect, useRef } from 'react';

export const StarBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationFrameId: number;
    let stars: Star[] = [];
    const starCount = 800; // Original count

    class Star {
      x: number;
      y: number;
      size: number;
      speed: number;
      opacity: number;
      baseOpacity: number;
      twinkleSpeed: number;

      constructor(width: number, height: number) {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = Math.random() * 1.5; // Slightly larger, softer stars
        this.speed = Math.random() * 0.2; // Original organic movement speed
        this.baseOpacity = Math.random() * 0.5 + 0.1;
        this.opacity = this.baseOpacity;
        this.twinkleSpeed = Math.random() * 0.01;
      }

      update(width: number, height: number) {
        this.y -= this.speed;
        
        if (this.y < 0) {
          this.y = height;
          this.x = Math.random() * width;
        }

        this.opacity += this.twinkleSpeed;
        if (this.opacity > this.baseOpacity + 0.3 || this.opacity < this.baseOpacity - 0.3) {
          this.twinkleSpeed = -this.twinkleSpeed;
        }
        
        if (this.opacity < 0) this.opacity = 0;
        if (this.opacity > 1) this.opacity = 1;
      }

      draw(context: CanvasRenderingContext2D) {
        context.beginPath();
        context.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        context.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
        context.fill();
      }
    }

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      stars = [];
      for (let i = 0; i < starCount; i++) {
        stars.push(new Star(canvas.width, canvas.height));
      }
    };

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      stars.forEach(star => {
        star.update(canvas.width, canvas.height);
        star.draw(ctx);
      });
      animationFrameId = requestAnimationFrame(render);
    };

    window.addEventListener('resize', resize);
    resize();
    render();

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div className="fixed inset-0 z-[-1] pointer-events-none bg-black-950">
      {/* 1. Deep Space Black Base */}
      <div className="absolute inset-0 bg-[#020202]" />

      {/* 2. Restored Purple Nebula (Top Left/Center) */}
      <div 
        className="absolute top-[-10%] left-[-10%] w-[70vw] h-[70vh] rounded-full opacity-20 blur-[120px]"
        style={{
            background: 'radial-gradient(circle, rgba(88, 28, 135, 0.4) 0%, transparent 70%)'
        }}
      />

      {/* 3. Restored Gold Nebula (Bottom Right/Center) */}
      <div 
        className="absolute bottom-[-10%] right-[-10%] w-[60vw] h-[60vh] rounded-full opacity-10 blur-[100px]"
        style={{
            background: 'radial-gradient(circle, rgba(212, 175, 55, 0.3) 0%, transparent 70%)'
        }}
      />

      {/* 4. Canvas Stars */}
      <canvas 
        ref={canvasRef} 
        className="absolute inset-0 w-full h-full"
      />
      
      {/* 5. Vignette Overlay for Depth */}
      <div className="absolute inset-0 bg-[radial-gradient(transparent_0%,#000000_100%)] opacity-80" />
    </div>
  );
};
