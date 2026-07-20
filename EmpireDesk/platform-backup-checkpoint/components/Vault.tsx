
import React, { useState, useRef } from 'react';
import { VaultItem, VaultItemType } from '../types';
import { 
  Folder, FileText, Image as ImageIcon, Video, File, HardDrive, 
  ChevronRight, Upload, Search, Download, Trash2, MoreVertical, 
  Share2, ArrowLeft, Home, Music, Check, Copy
} from 'lucide-react';
import { Button } from './ui/Button';

// Mock Initial Data
const INITIAL_ITEMS: VaultItem[] = [
    // Root Folders
    { id: 'f-1', parentId: null, name: 'Clienti', type: 'FOLDER', updatedAt: '2024-03-10', owner: 'Admin' },
    { id: 'f-2', parentId: null, name: 'Marketing Assets', type: 'FOLDER', updatedAt: '2024-03-12', owner: 'Gael' },
    { id: 'f-3', parentId: null, name: 'Contratti & Legale', type: 'FOLDER', updatedAt: '2024-02-28', owner: 'Maximilian' },
    { id: 'f-4', parentId: null, name: 'Risorse Interne', type: 'FOLDER', updatedAt: '2024-03-01', owner: 'Admin' },

    // Inside Clients (f-1)
    { id: 'f-1-1', parentId: 'f-1', name: 'Digital Spa', type: 'FOLDER', updatedAt: '2024-03-15', owner: 'Maximilian' },
    { id: 'f-1-2', parentId: 'f-1', name: 'E-com Brand X', type: 'FOLDER', updatedAt: '2024-03-14', owner: 'Gael' },

    // Inside Marketing (f-2)
    { id: 'doc-1', parentId: 'f-2', name: 'Brand_Kit_v2.pdf', type: 'PDF', size: '2.4 MB', updatedAt: '2024-03-12', owner: 'Gael' },
    { id: 'img-1', parentId: 'f-2', name: 'Logo_Main.png', type: 'IMAGE', size: '500 KB', updatedAt: '2024-03-12', owner: 'Gael' },
    { id: 'vid-1', parentId: 'f-2', name: 'Promo_Reel_Q1.mp4', type: 'VIDEO', size: '45 MB', updatedAt: '2024-03-10', owner: 'Leonardo' },
];

export const Vault: React.FC = () => {
  const [currentPath, setCurrentPath] = useState<VaultItem[]>([]);
  const [items, setItems] = useState<VaultItem[]>(INITIAL_ITEMS);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedItem, setSelectedItem] = useState<VaultItem | null>(null);
  const [isCopied, setIsCopied] = useState(false);
  
  // Hidden input ref for file selection
  const fileInputRef = useRef<HTMLInputElement>(null);

  const currentFolderId = currentPath.length > 0 ? currentPath[currentPath.length - 1].id : null;

  const filteredItems = items.filter(item => {
      // If searching, ignore folder structure
      if (searchQuery) {
          return item.name.toLowerCase().includes(searchQuery.toLowerCase());
      }
      return item.parentId === currentFolderId;
  });

  // ICONS STYLE: Premium Dark Steel/Silver for Folders
  const getIcon = (type: VaultItemType) => {
      switch(type) {
          case 'FOLDER': return <Folder className="w-12 h-12 text-slate-700 fill-slate-700/10 drop-shadow-sm" />;
          case 'PDF': return <FileText className="w-12 h-12 text-red-700 drop-shadow-sm" />;
          case 'IMAGE': return <ImageIcon className="w-12 h-12 text-blue-700 drop-shadow-sm" />;
          case 'VIDEO': return <Video className="w-12 h-12 text-purple-700 drop-shadow-sm" />;
          case 'ARCHIVE': return <Music className="w-12 h-12 text-pink-700 drop-shadow-sm" />; 
          default: return <File className="w-12 h-12 text-slate-600 drop-shadow-sm" />;
      }
  };

  const navigateTo = (folder: VaultItem) => {
      if (folder.type !== 'FOLDER') return;
      setCurrentPath([...currentPath, folder]);
      setSearchQuery(''); // Clear search on nav
  };

  const navigateUp = () => {
      setCurrentPath(prev => prev.slice(0, -1));
  };

  const navigateBreadcrumb = (index: number) => {
      setCurrentPath(prev => prev.slice(0, index + 1));
  };

  const navigateRoot = () => {
      setCurrentPath([]);
  };

  // --- REAL UPLOAD LOGIC ---
  const handleUploadClick = () => {
      fileInputRef.current?.click();
  };

  const formatSize = (bytes: number) => {
      if (bytes === 0) return '0 Bytes';
      const k = 1024;
      const sizes = ['Bytes', 'KB', 'MB', 'GB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const getFileType = (file: File): VaultItemType => {
      if (file.type.startsWith('image/')) return 'IMAGE';
      if (file.type.startsWith('video/')) return 'VIDEO';
      if (file.type === 'application/pdf') return 'PDF';
      if (file.type.includes('zip') || file.type.includes('compressed')) return 'ARCHIVE';
      return 'DOC';
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (!file) return;

      // Create a local object URL for preview and download
      const objectUrl = URL.createObjectURL(file);

      const newItem: VaultItem = {
          id: `file-${Date.now()}`,
          parentId: currentFolderId,
          name: file.name,
          type: getFileType(file),
          size: formatSize(file.size),
          updatedAt: new Date().toISOString().split('T')[0],
          owner: 'Maximilian',
          url: objectUrl // Store the blob URL
      };

      setItems(prev => [...prev, newItem]);
      
      // Reset input value
      if (fileInputRef.current) {
          fileInputRef.current.value = '';
      }
  };

  // --- ACTIONS LOGIC ---

  const handleDeleteItem = (itemId: string) => {
      if(confirm('Sei sicuro di voler eliminare permanentemente questa risorsa?')) {
          setItems(prev => prev.filter(i => i.id !== itemId));
          setSelectedItem(null); // Close modal
      }
  };

  const handleDownload = () => {
      if (selectedItem?.url) {
          const link = document.createElement('a');
          link.href = selectedItem.url;
          link.download = selectedItem.name;
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
      } else {
          alert("Attenzione: Questo è un file demo. La funzione download è attiva solo per i file caricati realmente in questa sessione.");
      }
  };

  const handleShare = () => {
      if (selectedItem) {
          // Mock link generation
          const link = `https://vault.aureus.os/share/${selectedItem.id}?token=${Math.random().toString(36).substring(7)}`;
          navigator.clipboard.writeText(link);
          setIsCopied(true);
          setTimeout(() => setIsCopied(false), 2000);
      }
  };

  // Stats
  const totalFiles = items.filter(i => i.type !== 'FOLDER').length;
  const storageUsed = `${(4.2 + (totalFiles * 0.05)).toFixed(2)} GB`; 

  // --- PLATINUM SILVER THEME DEFINITION ---
  // Clean, high-quality silver with strong borders and shadows
  const platinumCardClass = `
    bg-gradient-to-br from-[#F8FAFC] via-[#E2E8F0] to-[#94A3B8] 
    border-t border-l border-white/60 border-b border-r border-slate-400/50 
    rounded-sm p-4 flex flex-col items-center justify-between 
    transition-all duration-300 group cursor-pointer relative h-48 
    shadow-xl hover:-translate-y-1 hover:shadow-2xl overflow-hidden
  `;

  return (
    <div className="h-[calc(100vh-140px)] flex flex-col animate-in fade-in duration-500">
        
        {/* Hidden Input for File Selection */}
        <input 
            type="file" 
            ref={fileInputRef} 
            className="hidden" 
            onChange={handleFileChange} 
        />

        {/* Header Bar */}
        <div className="flex justify-between items-center border-b border-white/5 pb-6 mb-6">
            <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-white/10 border border-white/20 rounded-lg flex items-center justify-center backdrop-blur-md">
                    <HardDrive className="w-6 h-6 text-white" />
                </div>
                <div>
                    <h1 className="text-2xl font-bold text-silver-gradient tracking-tight">The Vault</h1>
                    <p className="text-xs text-platinum-500 font-mono">SECURE ASSET MANAGEMENT • {storageUsed} USED</p>
                </div>
            </div>
            <div className="flex gap-4">
                <div className="relative">
                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-platinum-600" />
                    <input 
                        className="bg-[#0A0A0A] border border-white/10 rounded-sm pl-10 pr-4 py-2.5 text-sm text-white focus:border-white/50 outline-none w-64 transition-all shadow-inner"
                        placeholder="Cerca file..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                    />
                </div>
                <Button variant="diamond" icon={<Upload className="w-4 h-4" />} onClick={handleUploadClick}>UPLOAD</Button>
            </div>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 bg-[#0A0A0A] border border-white/10 rounded-sm overflow-hidden flex flex-col relative shadow-2xl">
            
            {/* Breadcrumbs */}
            <div className="bg-[#0F0F0F] border-b border-white/5 px-6 py-3 flex items-center gap-2 text-sm">
                <button onClick={navigateRoot} className="p-1 hover:bg-white/5 rounded text-platinum-500 hover:text-white transition-colors">
                    <Home className="w-4 h-4" />
                </button>
                {currentPath.length > 0 && <ChevronRight className="w-4 h-4 text-platinum-700" />}
                
                {currentPath.map((folder, index) => (
                    <React.Fragment key={folder.id}>
                        <button 
                            onClick={() => navigateBreadcrumb(index)}
                            className={`font-medium hover:text-white transition-colors ${index === currentPath.length - 1 ? 'text-white' : 'text-platinum-500'}`}
                        >
                            {folder.name}
                        </button>
                        {index < currentPath.length - 1 && <ChevronRight className="w-4 h-4 text-platinum-700" />}
                    </React.Fragment>
                ))}
            </div>

            {/* Grid View */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-6">
                {searchQuery && (
                    <div className="mb-6 text-xs text-platinum-500 uppercase tracking-widest">
                        Risultati ricerca per "{searchQuery}"
                    </div>
                )}

                <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
                    {currentPath.length > 0 && !searchQuery && (
                        <button 
                            onClick={navigateUp}
                            className={`${platinumCardClass} opacity-80 hover:opacity-100`}
                        >
                            <div className="flex-1 flex flex-col items-center justify-center gap-3 w-full">
                                <ArrowLeft className="w-12 h-12 text-slate-600" />
                                <span className="text-xs font-black text-slate-700 uppercase tracking-widest">Indietro</span>
                            </div>
                        </button>
                    )}

                    {filteredItems.map(item => (
                        <div 
                            key={item.id}
                            onClick={() => item.type === 'FOLDER' ? navigateTo(item) : setSelectedItem(item)}
                            className={platinumCardClass}
                        >
                            {/* Realistic Noise Texture */}
                            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.08] pointer-events-none mix-blend-overlay"></div>
                            
                            {/* Shine Effect */}
                            <div className="absolute top-0 right-0 w-32 h-32 bg-white opacity-[0.3] rounded-full blur-2xl -translate-y-12 translate-x-12 group-hover:opacity-[0.5] transition-opacity pointer-events-none"></div>

                            <div className="flex-1 flex items-center justify-center group-hover:scale-110 transition-transform duration-300 w-full overflow-hidden relative z-10">
                                {/* Thumbnail Preview for Images in Grid */}
                                {item.type === 'IMAGE' && item.url ? (
                                    <div className="w-full h-full p-2 bg-white/20 rounded-sm border border-white/30 shadow-inner">
                                        <img src={item.url} alt={item.name} className="w-full h-full object-cover opacity-90 group-hover:opacity-100 rounded-sm shadow-sm" />
                                    </div>
                                ) : (
                                    getIcon(item.type)
                                )}
                            </div>
                            
                            <div className="w-full text-center mt-4 relative z-10 border-t border-slate-900/5 pt-3">
                                <p className="text-xs font-black text-slate-900 truncate w-full tracking-tight drop-shadow-sm" title={item.name}>{item.name}</p>
                                <p className="text-[10px] text-slate-600 font-bold uppercase tracking-wider mt-1">{item.type === 'FOLDER' ? item.updatedAt : item.size}</p>
                            </div>
                            
                            {/* Context Menu Trigger */}
                            <div className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
                                <button className="p-1 hover:bg-slate-900/10 rounded text-slate-500 hover:text-slate-900">
                                    <MoreVertical className="w-4 h-4" />
                                </button>
                            </div>
                        </div>
                    ))}
                </div>

                {filteredItems.length === 0 && (
                    <div className="flex flex-col items-center justify-center h-full text-platinum-600">
                        <Folder className="w-20 h-20 mb-6 opacity-20 text-white" />
                        <p className="text-sm uppercase tracking-widest font-bold">Cartella Vuota</p>
                        <Button variant="outline" size="sm" className="mt-4 border-white/10" onClick={handleUploadClick}>Carica primo file</Button>
                    </div>
                )}
            </div>

            {/* Bottom Bar Stats */}
            <div className="bg-[#0F0F0F] border-t border-white/5 px-6 py-2 flex justify-between items-center text-[10px] text-platinum-600 font-mono uppercase tracking-widest">
                <span>{items.length} Elementi totali nel Vault</span>
                <span className="flex items-center gap-2"><div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div> ENCRYPTED</span>
            </div>
        </div>

        {/* File Preview Modal */}
        {selectedItem && (
            <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/95 backdrop-blur-xl animate-in fade-in duration-200">
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm shadow-2xl w-full max-w-5xl h-[85vh] flex flex-col relative">
                    
                    {/* Modal Header */}
                    <div className="flex justify-between items-center p-6 border-b border-white/5 bg-[#0F0F0F]">
                        <div className="flex items-center gap-4">
                            <div className="p-2 bg-white/5 rounded-sm">
                                {getIcon(selectedItem.type)}
                            </div>
                            <div>
                                <h3 className="text-xl font-bold text-white max-w-md truncate">{selectedItem.name}</h3>
                                <p className="text-xs text-platinum-500 uppercase tracking-widest font-mono">
                                    {selectedItem.size} • Uploaded by {selectedItem.owner} • {selectedItem.updatedAt}
                                </p>
                            </div>
                        </div>
                        <div className="flex gap-3">
                            <Button 
                                variant="outline" 
                                icon={isCopied ? <Check className="w-4 h-4 text-green-400"/> : <Share2 className="w-4 h-4"/>} 
                                onClick={handleShare}
                            >
                                {isCopied ? 'Copiato' : 'Share'}
                            </Button>
                            
                            <Button variant="diamond" icon={<Download className="w-4 h-4"/>} onClick={handleDownload}>
                                Download
                            </Button>
                            
                            <div className="h-8 w-[1px] bg-white/10 mx-2"></div>
                            
                            <button onClick={() => handleDeleteItem(selectedItem.id)} className="p-2 bg-red-900/10 border border-red-900/30 hover:bg-red-900/30 rounded text-red-400 transition-colors">
                                <Trash2 className="w-5 h-5"/>
                            </button>
                            <button onClick={() => setSelectedItem(null)} className="p-2 hover:bg-white/10 rounded text-platinum-500 hover:text-white transition-colors">
                                <span className="sr-only">Close</span>
                                <div className="text-sm font-bold uppercase tracking-wider">ESC</div>
                            </button>
                        </div>
                    </div>
                    
                    {/* Preview Area */}
                    <div className="flex-1 flex items-center justify-center bg-[#050505] p-8 overflow-hidden relative">
                        {/* Dot Grid Background */}
                        <div className="absolute inset-0 bg-[linear-gradient(#111_1px,transparent_1px),linear-gradient(90deg,#111_1px,transparent_1px)] bg-[size:20px_20px] pointer-events-none opacity-20"></div>

                        {selectedItem.type === 'IMAGE' ? (
                            selectedItem.url ? (
                                <img src={selectedItem.url} alt={selectedItem.name} className="max-w-full max-h-full object-contain shadow-2xl rounded-sm border border-white/5" />
                            ) : (
                                <div className="text-center text-platinum-500">
                                    <ImageIcon className="w-24 h-24 mx-auto mb-4 opacity-20" />
                                    <p className="text-sm uppercase tracking-widest">Anteprima immagine non disponibile (Demo)</p>
                                </div>
                            )
                        ) : selectedItem.type === 'VIDEO' ? (
                            selectedItem.url ? (
                                <video src={selectedItem.url} controls className="max-w-full max-h-full shadow-2xl rounded-sm border border-white/5" />
                            ) : (
                                <div className="text-center text-platinum-500">
                                    <Video className="w-24 h-24 mx-auto mb-4 opacity-20" />
                                    <p className="text-sm uppercase tracking-widest">Anteprima video non disponibile (Demo)</p>
                                </div>
                            )
                        ) : selectedItem.type === 'PDF' ? (
                             <div className="text-center text-platinum-500 bg-white/5 p-20 rounded-sm border border-white/5">
                                <FileText className="w-24 h-24 mx-auto mb-4 opacity-50 text-red-400" />
                                <p className="text-lg font-bold text-white mb-2">{selectedItem.name}</p>
                                <p className="text-xs uppercase tracking-widest mb-6">Documento PDF</p>
                                <Button variant="outline" size="sm" onClick={handleDownload}>Scarica per visualizzare</Button>
                            </div>
                        ) : (
                            <div className="text-center">
                                <File className="w-24 h-24 mx-auto mb-4 text-platinum-700" />
                                <p className="text-sm text-platinum-500 uppercase tracking-widest">Anteprima non disponibile per questo formato.</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        )}
    </div>
  );
};
