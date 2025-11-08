# Тестирование в Дата-инженерии | Testing in Data Engineering

https://www.notion.so/korsak0v/Data-Engineer-185c62fdf79345eb9da9928356884ea0

## О видео

## О проекте

### О тестировании

Тестирование – это инструмент контроля качества кода и бизнес-логики. Для дата-инженера тесты позволяют:

- **Своевременно находить ошибки** на этапе разработки, а не на проде.
- **Гарантировать корректность обработки данных** – ошибки в пайплайнах могут влиять на отчёты, решения и деньги.
- **Экономить время и ресурсы** – автоматические тесты быстро проверяют весь проект, сокращая ручную работу и расходы на
  исправление багов.
- **Повышать доверие к продукту** – со стороны команды аналитиков, заказчиков и бизнеса.
- **Упрощать развитие и поддержку кода** – тесты защищают от случайных поломок при изменениях и позволяют эффективно
  работать в команде.

Хорошие тесты – уверенность в качестве данных и стабильной работе всей дата-инфраструктуры.


<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Определение градиентов -->
  <defs>
    <linearGradient id="unitGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#4CAF50;stop-opacity:0.9" />
      <stop offset="100%" style="stop-color:#45a049;stop-opacity:0.9" />
    </linearGradient>
    <linearGradient id="integrationGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#2196F3;stop-opacity:0.9" />
      <stop offset="100%" style="stop-color:#1976D2;stop-opacity:0.9" />
    </linearGradient>
    <linearGradient id="e2eGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#FF9800;stop-opacity:0.9" />
      <stop offset="100%" style="stop-color:#F57C00;stop-opacity:0.9" />
    </linearGradient>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">
      <polygon points="0 0, 10 5, 0 10" fill="#666"/>
    </marker>
  </defs>
  
  <!-- Заголовок -->
  <text x="400" y="40" font-family="Arial, sans-serif" font-size="28" font-weight="bold" text-anchor="middle" fill="#333">
    Пирамида тестирования
  </text>
  
  <!-- Вершина пирамиды: x=400, y=80 -->
  <!-- Основание пирамиды: левый угол x=125, y=520, правый угол x=675, y=520 -->
  <!-- Высота = 440, делим на 3 части: 146.67 каждая -->
  
  <!-- E2E тесты (верхняя треть) -->
  <!-- y1 = 80, y2 = 80 + 146.67 = 226.67 -->
  <!-- Ширина на y=226.67: пропорционально (226.67-80)/440 = 0.333, ширина = 550 * 0.333 = 183.33 с каждой стороны -->
  <polygon points="400,80 308.33,226.67 491.67,226.67" fill="url(#e2eGrad)" stroke="#E65100" stroke-width="2"/>
  <text x="400" y="130" font-family="Arial, sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="white" stroke="#000000">
    E2E тесты
  </text>
  <text x="400" y="155" font-family="Arial, sans-serif" font-size="13" text-anchor="middle" fill="white">
    Сквозные
  </text>
  <text x="400" y="175" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Медленно • Дорого
  </text>
  <text x="400" y="195" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Полный процесс
  </text>
  
  <!-- Разделительная линия -->
  <line x1="308.33" y1="226.67" x2="491.67" y2="226.67" stroke="#333" stroke-width="2"/>
  
  <!-- Интеграционные тесты (средняя треть) -->
  <!-- y2 = 226.67, y3 = 226.67 + 146.67 = 373.33 -->
  <!-- Ширина на y=373.33: пропорционально (373.33-80)/440 = 0.667, ширина = 550 * 0.667 = 366.67 с каждой стороны -->
  <polygon points="308.33,226.67 216.67,373.33 583.33,373.33 491.67,226.67" fill="url(#integrationGrad)" stroke="#1565C0" stroke-width="2"/>
  <text x="400" y="280" font-family="Arial, sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="white" stroke="#000000">
    Интеграционные
  </text>
  <text x="400" y="305" font-family="Arial, sans-serif" font-size="13" text-anchor="middle" fill="white">
    API + БД + Очереди
  </text>
  <text x="400" y="330" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Средняя скорость
  </text>
  <text x="400" y="350" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Части системы вместе
  </text>
  
  <!-- Разделительная линия -->
  <line x1="216.67" y1="373.33" x2="583.33" y2="373.33" stroke="#333" stroke-width="2"/>
  
  <!-- Юнит-тесты (нижняя треть) -->
  <!-- y3 = 373.33, y4 = 520 -->
  <polygon points="216.67,373.33 125,520 675,520 583.33,373.33" fill="url(#unitGrad)" stroke="#2E7D32" stroke-width="2"/>
  <text x="400" y="425" font-family="Arial, sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="white" stroke="#000000">
    Юнит-тесты
  </text>
  <text x="400" y="455" font-family="Arial, sans-serif" font-size="13" text-anchor="middle" fill="white">
    Функции • Классы • Модули
  </text>
  <text x="400" y="480" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Быстро • Просто • Много
  </text>
  <text x="400" y="500" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="white">
    Основа пирамиды
  </text>
  
  <!-- Контур основного треугольника -->
  <polygon points="400,80 125,520 675,520" fill="none" stroke="#333" stroke-width="3"/>
  
  <!-- Пояснительные стрелки и текст -->
  <g opacity="0.8">
    <!-- Стрелка вверх - стоимость -->
    <line x1="120" y1="500" x2="120" y2="100" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
    <text x="80" y="310" font-family="Arial, sans-serif" font-size="14" fill="#666" transform="rotate(-90 125 300)">
      Стоимость и время ↑
    </text>
    
    <!-- Стрелка вниз - количество -->
    <line x1="680" y1="100" x2="680" y2="500" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
    <text x="590" y="320" font-family="Arial, sans-serif" font-size="14" fill="#666" transform="rotate(90 685 300)">
      Количество тестов ↑
    </text>
  </g>
</svg>

### Виртуальное окружение

Настройка виртуального окружения:

```bash
python3.13 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install poetry && \
poetry lock && \
poetry install
```