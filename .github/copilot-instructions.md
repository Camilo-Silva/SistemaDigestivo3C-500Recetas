# Instrucciones — Landing SD3C (Shopify Liquid)

## Contexto del proyecto
Landing page de venta para "500 Recetas Sin Pensar | Sistema Digestivo 3C" de Vida en Calma.
- **HTML de referencia**: `index-Sistema-Digestivo3C.html` — fuente de verdad para contenido y estilos
- **Archivos liquid**: `section-liquid/sd3c-*.liquid` — una sección por archivo, para usar en Shopify
- **GitHub**: `https://github.com/Camilo-Silva/SistemaDigestivo3C-500Recetas.git`, rama `main`

---

## Reglas para crear archivos `.liquid`

### Estructura de cada archivo
```
<style> ... </style>
{{ 'URL_FONT_AWESOME' | stylesheet_tag }}   ← solo si la sección usa íconos FA
HTML con {{ section.settings.CAMPO }}
<script> ... </script>                      ← solo si la sección necesita JS
{% schema %} ... {% endschema %}
```

### Nombres de schema
- Máximo 20 caracteres (límite de Shopify)
- Formato: `"SD3C NombreCorto"`

### Imágenes configurables
```liquid
{% if section.settings.img_X != blank %}
  <img src="{{ section.settings.img_X | img_url: 'master' }}" alt="...">
{% endif %}
```
Schema: `"type": "image_picker"`

### URLs / CTAs configurables
Schema: `"type": "url"` → en HTML: `href="{{ section.settings.cta_url }}"`

### Prefijo CSS obligatorio
Todas las clases CSS llevan prefijo `sd3c-` para evitar conflictos con el tema de Shopify.
Ejemplo: `.sd3c-hero`, `.sd3c-pricing-box`, `.sd3c-faq-item`

---

## ⚠️ REGLA CRÍTICA: font-size solo en `px`, nunca en `rem`

**Problema**: Muchos temas Shopify setean `html { font-size: 62.5% }`, lo que hace que
`1rem = 10px`. Eso vuelve ilegibles todos los textos con `rem`:
- `.9rem` → 9px ❌
- `.82rem` → 8px ❌
- `.75rem` → 7.5px ❌

**Solución**: Usar siempre `px` explícitos en `font-size`.

### Tabla de conversión (base 16px → px):
| rem | px |
|-----|----|
| `.65rem` | `11px` |
| `.7rem` | `11px` |
| `.72rem` | `12px` |
| `.75rem` | `12px` |
| `.78rem` | `13px` |
| `.8rem` | `13px` |
| `.82rem` | `13px` |
| `.85rem` | `14px` |
| `.87rem` | `14px` |
| `.88rem` | `14px` |
| `.9rem` | `15px` |
| `.92rem` | `15px` |
| `.93rem` | `15px` |
| `.95rem` | `15px` |
| `.97rem` | `15px` |
| `1rem` | `16px` |
| `1.05rem` | `17px` |
| `1.1rem` | `18px` |
| `1.2rem` | `19px` |
| `1.3rem` | `21px` |
| `1.35rem` | `22px` |
| `1.5rem` | `24px` |
| `1.6rem` | `26px` |
| `1.8rem` | `29px` |
| `2rem` | `32px` |
| `2.5rem` | `40px` |
| `2.8rem` | `45px` |
| `4.5rem` | `72px` |

**Excepción permitida**: `clamp(NNpx, Nvw, NNpx)` — usar siempre con `px` dentro del clamp, nunca rem.

---

## Variables CSS estándar (incluir en cada archivo)

```css
:root {
  --verde:       #7a9d8e;
  --verde-claro: #9dbcb3;
  --verde-fondo: #eaf4f0;
  --rosa:        #d8a7b1;
  --rojo:        #c4757f;
  --gris-oscuro: #1C1C1E;
  --gris-medio:  #4A4A4A;
  --gris-suave:  #a39384;
  --blanco:      #FFFFFF;
  --fondo:       #f1ebe5;
  --radio:       14px;
  --sombra:      0 4px 24px rgba(122,157,142,.12);
}
```

---

## Orden de las 24 secciones en el template

| # | Archivo |
|---|---------|
| 1 | `sd3c-ticker.liquid` |
| 2 | `sd3c-cabecera.liquid` |
| 3 | `sd3c-vsl.liquid` |
| 4 | `sd3c-hero.liquid` |
| 5 | `sd3c-dolor.liquid` |
| 6 | `sd3c-solucion.liquid` |
| 7 | `sd3c-beneficios.liquid` |
| 8 | `sd3c-testimonials.liquid` |
| 9 | `sd3c-incluye.liquid` |
| 10 | `sd3c-producto.liquid` |
| 11 | `sd3c-pricing.liquid` |
| 12 | `sd3c-bonus.liquid` |
| 13 | `sd3c-extras.liquid` |
| 14 | `sd3c-regalo.liquid` |
| 15 | `sd3c-objeciones.liquid` |
| 16 | `sd3c-forwho.liquid` |
| 17 | `sd3c-urgencia.liquid` |
| 18 | `sd3c-payment.liquid` |
| 19 | `sd3c-garantia.liquid` |
| 20 | `sd3c-cierre.liquid` |
| 21 | `sd3c-faq.liquid` |
| 22 | `sd3c-footer.liquid` |
| 23 | `sd3c-float-cta.liquid` |
| 24 | `sd3c-toast.liquid` |

> `sd3c-float-cta` y `sd3c-toast` van al final pero se renderizan encima de todo por `position: fixed`.

---

## IDs y JS importantes

| ID | Uso |
|----|-----|
| `sd3c-h` / `sd3c-m` / `sd3c-s` | Countdown en pricing |
| `sd3c-live-count` | Contador de visitas en pricing |
| `sd3cToastContainer` | Contenedor de toasts |
| `sd3cVslVideo` / `sd3cVslWrap` | Video VSL |

- **Countdown key**: `'vc_sd3c_countdown_v1'` (sessionStorage, 15 min)
- **Live viewers pool**: `[7, 8, 9, 11, 12, 14, 16, 19]`, intervalo 4500ms
- **Toast**: delay inicial 30000ms, luego `25000 + Math.random() * 15000`

---

## Imágenes de referencia

| Imagen | Ruta local |
|--------|-----------|
| Portada recetario | `image/SIstema Digestivo3C/Portada.jpg` |
| Plantilla Notion | `image/SIstema Digestivo3C/Sistema de planificación de comidas organizado.png` |
| App Vida en Calma | `image/SIstema Digestivo3C/App Vida en Calma_ decisiones fáciles.png` |
| Garantía 7 días | `image/SIstema Digestivo3C/7 días garantía en oro.png` |
| Ebook regalo | `image/EbookRegalo/Dejar costumbres que te estancan.png` |
| MercadoLíder | `image/ML.png` |
| Métodos de pago | `image/MetodosPago.png` |

---

## Fixes aplicados durante el desarrollo

- **rem → px**: Todos los `font-size` convertidos a px en los 11 archivos que lo tenían mal.
- **sd3c-payment**: Fondo cambiado a `#FFFFFF` (era `var(--fondo)` beige).
- **sd3c-bonus**: Reescrita para coincidir con el index — estructura banda lateral + 3 cards ricas con features grid y lista de mercado; schema con 3 image_pickers (`img_portada`, `img_notion`, `img_app`).
- **sd3c-pricing**: IDs del countdown renombrados a `sd3c-h/m/s` y live counter a `sd3c-live-count` para evitar conflictos con otras secciones en la misma página.
