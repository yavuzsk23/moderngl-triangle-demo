# ModernGL Triangle Demo

A minimal OpenGL demo built with **ModernGL** and **moderngl-window**. Renders a triangle whose colors animate continuously using a time-based fragment shader.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenGL](https://img.shields.io/badge/OpenGL-3.3-red)
![ModernGL](https://img.shields.io/badge/ModernGL-GPU%20Rendering-purple)

---

## 🇬🇧 English

### Overview
This project renders a single triangle directly on the GPU using a custom vertex and fragment shader pair. The fragment shader uses `sin()` and `cos()` of the elapsed time to continuously shift the triangle's colors, producing a simple animated effect.

### Features
- Direct GPU rendering via raw GLSL shaders (vertex + fragment)
- Per-vertex color interpolation
- Time-based color animation using a shader uniform
- Minimal, dependency-light OpenGL setup via `moderngl-window`

### Requirements
- Python 3.10 or higher
- `moderngl`
- `moderngl-window`
- `numpy`

### Installation
```bash
pip install moderngl moderngl-window numpy
```

### Usage
```bash
python moderngl_triangle.py
```

A window will open showing a triangle with continuously shifting colors.

### How it works
Three vertices are defined, each carrying a 2D position and an RGB color, packed into a single NumPy array and uploaded to the GPU via `self.ctx.buffer(...)`. The vertex shader passes position and color through unchanged; the fragment shader receives the interpolated color for each pixel and modulates its red and blue channels using `sin(time)` and `cos(time)`, where `time` is passed in every frame as a shader uniform. The main render loop must be named `render(self, time, frame_time)` — `moderngl-window` calls this exact method name each frame; naming it anything else (e.g. `on_render`) means nothing gets drawn, with no error raised.

Note: This project was developed with AI assistance as part of my learning process

---

## 🇩🇪 Deutsch

### Überblick
Dieses Projekt rendert ein einzelnes Dreieck direkt auf der GPU mithilfe eines benutzerdefinierten Vertex- und Fragment-Shader-Paars. Der Fragment-Shader verwendet `sin()` und `cos()` der verstrichenen Zeit, um die Farben des Dreiecks kontinuierlich zu verändern, was einen einfachen Animationseffekt erzeugt.

### Funktionen
- Direktes GPU-Rendering über rohe GLSL-Shader (Vertex + Fragment)
- Farbinterpolation pro Vertex
- Zeitbasierte Farbanimation über eine Shader-Uniform
- Minimales, abhängigkeitsarmes OpenGL-Setup über `moderngl-window`

### Voraussetzungen
- Python 3.10 oder höher
- `moderngl`
- `moderngl-window`
- `numpy`

### Installation
```bash
pip install moderngl moderngl-window numpy
```

### Verwendung
```bash
python moderngl_triangle.py
```

Ein Fenster öffnet sich mit einem Dreieck, dessen Farben sich kontinuierlich verändern.

### Funktionsweise
Drei Vertices werden definiert, jeweils mit einer 2D-Position und einer RGB-Farbe, gepackt in ein einzelnes NumPy-Array und über `self.ctx.buffer(...)` auf die GPU hochgeladen. Der Vertex-Shader gibt Position und Farbe unverändert weiter; der Fragment-Shader empfängt die interpolierte Farbe für jedes Pixel und moduliert dessen roten und blauen Kanal mit `sin(time)` und `cos(time)`, wobei `time` jeden Frame als Shader-Uniform übergeben wird. Die Haupt-Render-Schleife muss `render(self, time, frame_time)` heißen — `moderngl-window` ruft genau diesen Methodennamen bei jedem Frame auf; wird sie anders benannt (z. B. `on_render`), wird nichts gezeichnet, ohne dass ein Fehler ausgelöst wird.

Hinweis: Dieses Projekt wurde im Rahmen meines Lernprozesses mit KI-Unterstützung entwickelt

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu proje, özel bir vertex ve fragment shader çifti kullanarak doğrudan GPU üzerinde tek bir üçgen render eder. Fragment shader, geçen sürenin `sin()` ve `cos()` değerlerini kullanarak üçgenin renklerini sürekli değiştirir, basit bir animasyon efekti oluşturur.

### Özellikler
- Ham GLSL shader'lar (vertex + fragment) üzerinden doğrudan GPU render'ı
- Vertex başına renk interpolasyonu
- Bir shader uniform'u kullanarak zaman tabanlı renk animasyonu
- `moderngl-window` üzerinden minimal, az bağımlılıklı OpenGL kurulumu

### Gereksinimler
- Python 3.10 veya üzeri
- `moderngl`
- `moderngl-window`
- `numpy`

### Kurulum
```bash
pip install moderngl moderngl-window numpy
```

### Kullanım
```bash
python moderngl_triangle.py
```

Renkleri sürekli değişen bir üçgen gösteren bir pencere açılır.

### Nasıl çalışır?
Her biri 2D pozisyon ve RGB renk taşıyan üç vertex tanımlanır, tek bir NumPy dizisine paketlenir ve `self.ctx.buffer(...)` aracılığıyla GPU'ya yüklenir. Vertex shader, pozisyon ve rengi değiştirmeden aktarır; fragment shader her piksel için interpolasyona uğramış rengi alır ve kırmızı ile mavi kanallarını `sin(time)` ve `cos(time)` ile modüle eder, `time` değeri her karede bir shader uniform'u olarak geçirilir. Ana render döngüsü `render(self, time, frame_time)` adında olmalıdır — `moderngl-window` her karede tam olarak bu metod adını çağırır; farklı bir isim verilirse (örn. `on_render`), hiçbir hata verilmeden hiçbir şey çizilmez.

Not: Bu proje öğrenme sürecimin bir parçası olarak yapay zeka desteğiyle geliştirilmiştir
