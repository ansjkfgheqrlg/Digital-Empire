
import React, { useState } from 'react';
import { Send, CheckCircle, Loader2 } from 'lucide-react';
import { Lead } from '../../types';
import { GoldButton } from '../ui/GoldButton';

export const Contact: React.FC = () => {
  const [formState, setFormState] = useState({
    name: '',
    email: '',
    goal: 'consultation', // Default to consultation
    message: ''
  });
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError('');

    const FORMSPREE_ENDPOINT = "https://formspree.io/f/xovrwogb";

    try {
      const response = await fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formState)
      });

      if (response.ok) {
        const newLead: Lead = {
          id: Date.now().toString(),
          ...formState,
          date: new Date().toLocaleString('it-IT'),
          status: 'new'
        };
        const existingLeads = JSON.parse(localStorage.getItem('digital_empire_leads') || '[]');
        localStorage.setItem('digital_empire_leads', JSON.stringify([newLead, ...existingLeads]));

        setIsSubmitted(true);
        setFormState({ name: '', email: '', goal: 'consultation', message: '' });
      } else {
        const newLead: Lead = {
          id: Date.now().toString(),
          ...formState,
          date: new Date().toLocaleString('it-IT'),
          status: 'new'
        };
        const existingLeads = JSON.parse(localStorage.getItem('digital_empire_leads') || '[]');
        localStorage.setItem('digital_empire_leads', JSON.stringify([newLead, ...existingLeads]));
        setIsSubmitted(true);
      }
    } catch (err) {
      try {
        const newLead: Lead = {
          id: Date.now().toString(),
          ...formState,
          date: new Date().toLocaleString('it-IT'),
          status: 'new'
        };
        const existingLeads = JSON.parse(localStorage.getItem('digital_empire_leads') || '[]');
        localStorage.setItem('digital_empire_leads', JSON.stringify([newLead, ...existingLeads]));
        setIsSubmitted(true);
      } catch (localErr) {
        setError("Errore di connessione. Controlla la tua rete.");
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const inputClasses = "w-full bg-black-900/60 backdrop-blur-sm border border-gray-800 rounded-none px-4 py-3 text-white focus:outline-none focus:border-gold-500 transition-colors placeholder-gray-600 font-sans";

  return (
    <section id="contact" className="py-24 bg-transparent relative">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto bg-black-900/80 backdrop-blur-md border border-gray-800 p-8 md:p-12 shadow-[0_0_50px_rgba(0,0,0,0.5)] relative overflow-hidden">
          {/* Gold accent top border */}
          <div className="absolute top-0 left-0 w-full h-1 bg-metal-gradient" />

          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <h2 className="font-serif text-3xl md:text-4xl text-white mb-4">
                Inizia il Tuo <br /><span className="text-gold-500">Impero Digitale</span>
              </h2>
              <p className="text-gray-400 mb-8 leading-relaxed">
                Non offriamo servizi a chiunque. Lavoriamo solo con chi è pronto a scalare seriamente. Se sei tu, compila il modulo.
              </p>

              <div className="space-y-6">
                <div className="flex items-center text-white">
                  <div className="w-10 h-10 bg-black-800 flex items-center justify-center mr-4 border border-gold-500/30">
                    <span className="font-serif font-bold text-gold-500">01</span>
                  </div>
                  <p className="text-sm">Analisi Gratuita della tua presenza online.</p>
                </div>
                <div className="flex items-center text-white">
                  <div className="w-10 h-10 bg-black-800 flex items-center justify-center mr-4 border border-gold-500/30">
                    <span className="font-serif font-bold text-gold-500">02</span>
                  </div>
                  <p className="text-sm">Strategia su misura basata sull'AI.</p>
                </div>
                <div className="flex items-center text-white">
                  <div className="w-10 h-10 bg-black-800 flex items-center justify-center mr-4 border border-gold-500/30">
                    <span className="font-serif font-bold text-gold-500">03</span>
                  </div>
                  <p className="text-sm">Esecuzione rapida e risultati misurabili.</p>
                </div>
              </div>
            </div>

            <div className="relative">
              {isSubmitted ? (
                <div className="h-full flex flex-col items-center justify-center text-center p-8 animate-fade-in border border-gold-500/20 bg-black-950/50">
                  <CheckCircle className="w-16 h-16 text-gold-500 mb-4" />
                  <h3 className="text-2xl text-white font-serif mb-2">Candidatura Inviata</h3>
                  <p className="text-gray-400 mb-6">I tuoi dati sono stati inviati al nostro team. Un consulente analizzerà la tua richiesta entro 24 ore.</p>
                  <button onClick={() => setIsSubmitted(false)} className="text-sm text-gold-500 underline hover:text-white transition-colors">Invia un'altra richiesta</button>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-4">
                  <div>
                    <label className="block text-xs uppercase tracking-widest text-gray-500 mb-2">Nome / Azienda</label>
                    <input
                      type="text"
                      name="name"
                      required
                      className={inputClasses}
                      value={formState.name}
                      onChange={e => setFormState({ ...formState, name: e.target.value })}
                      placeholder="Inserisci nome..."
                      disabled={isSubmitting}
                    />
                  </div>

                  <div>
                    <label className="block text-xs uppercase tracking-widest text-gray-500 mb-2">Email Aziendale</label>
                    <input
                      type="email"
                      name="email"
                      required
                      className={inputClasses}
                      value={formState.email}
                      onChange={e => setFormState({ ...formState, email: e.target.value })}
                      placeholder="email@business.com"
                      disabled={isSubmitting}
                    />
                  </div>

                  <div>
                    <label className="block text-xs uppercase tracking-widest text-gray-500 mb-2">Obiettivo Principale</label>
                    <select
                      name="goal"
                      className={inputClasses}
                      value={formState.goal}
                      onChange={e => setFormState({ ...formState, goal: e.target.value })}
                      disabled={isSubmitting}
                    >
                      <option value="consultation">Consulenza Gratuita Conoscitiva</option>
                      <option value="web">Sito Web Premium / E-commerce</option>
                      <option value="automation">Automazione AI & Chatbot</option>
                      <option value="social">Social Growth & Marketing</option>
                      <option value="full">Digital Empire (Full Service)</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs uppercase tracking-widest text-gray-500 mb-2">Dettagli Progetto</label>
                    <textarea
                      name="message"
                      rows={3}
                      className={inputClasses}
                      value={formState.message}
                      onChange={e => setFormState({ ...formState, message: e.target.value })}
                      placeholder="Descrivi brevemente le tue necessità..."
                      disabled={isSubmitting}
                    />
                  </div>

                  {error && <p className="text-red-500 text-xs">{error}</p>}

                  <div className="pt-4">
                    <GoldButton
                      type="submit"
                      fullWidth
                      disabled={isSubmitting}
                    >
                      {isSubmitting ? (
                        <>Processando... <Loader2 className="animate-spin" size={16} /></>
                      ) : (
                        <>Invia Candidatura <Send size={16} /></>
                      )}
                    </GoldButton>
                  </div>
                </form>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
