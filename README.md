# module_1
Для основного набора данных был использован открытый датасет https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games

Веб-скрейпинг с сайта https://thegameawards.com/nominees

Первичная обработка данных: заполнены пропущенные значения, преобразованы форматы столбцов.

Проведен EDA и построены различные визуализации для основных признаков.

Возможные применения этих данных в контексте машинного обучения указаны в конце EDA.

# module_2
Разметка происходила на app.labelbox.com

ТЗ и сбор обратной связи по разметке данных находились в гугл форме (https://forms.gle/ZCuRHBRrucqDdM3V6)

Рассчет и оценка метрик согласованности и квалификации разметчиков и рефлексия на тему процесса разметки данных и качества полученных результатов представлены в ноутбуке AI or not AI.ipynb

# module_3
Выбор трека: Мультимодальные данные

В качестве исходного датасета был выбран CheXpert (https://www.kaggle.com/datasets/mimsadiislam/chexpert?select=CheXpert-v1.0-small), так как он уже размечен врачами (при всем желании, рентгены я размечаю плохо).

Исходный датасет состоит из изображений медицинских рентгеновских снимков и соответствующих им описаний в формате CSV-файлов. 


# module_4
Исследуя применение синтетических данных в медицине, я выделила два основных подхода, популярных на данный момент. Ниже я попыталась описать их на примере двух статей. 

1) https://medinform.jmir.org/2020/2/e16492
  Первая статья - Analyzing Medical Research Results Based on Synthetic Data and Their Relation to Real Data Results: Systematic Comparison From Five Observational Studies - является отличным примером того, как синтетические данные можно применить для сохранения конфиденциальности в рамках исследований. Врачебная тайна часто вставляла палки в колеса медицинским исследователям, но эта статья показывает, что синтетические данные могут стать неким компромиссом в этой проблеме.

  Используя систему MDClone, исследователи синтезировали структурированные медицинские данные, включая информацию о пациентах, их визитах, госпитализациях, диагнозах, лекарствах, процедурах и других параметрах, собранных из электронных медицинских записей (EMRs). Алгоритм использовал случайную выборку из статистических распределений, оцененных на основе реальных данных, чтобы создавать синтетические наборы данных с аналогичными статистическими характеристиками.

  Целью использования синтетических данных была проверка их валидности для медицинских исследований. Исследования, участвовавшие в эксперименте, включали оценку процента пропуска рекомендованных лекарств, влияния времени до проведения коронарного вмешательства на выживаемость после выписки, сравнение различных методов лечения сахарного диабета и оценку влияния уровня мочевины в крови на смертность после выписки пациентов с острой сердечной недостаточностью.

  В результате исследований было установлено, что синтетические данные, созданные системой MDClone, достаточно точно моделировали статистические характеристики реальных медицинских данных. Результаты анализов на синтетических данных были сопоставимы с результатами, полученными на основе реальных данных, что позволяет считать синтетические данные надежными и пригодными для использования в медицинских исследованиях (в пределах разумного, конечно).

  Этот подход может значительно ускорить процессы исследования, предоставив исследователям возможность проводить предварительные анализы и проверку гипотез, даже когда реальные данные еще не доступны из-за ограничений приватности и безопасности.
  
![Зачем? Затем](<img src="https://cs8.pikabu.ru/post_img/2016/12/20/5/og_og_1482216858253232392.jpg" width="50%" height="50%">)

2) https://www.sciencedirect.com/science/article/pii/S2666914522001476
  Вторая статья - SynthEye: Investigating the Impact of Synthetic Data on Artificial Intelligence-assisted Gene Diagnosis of Inherited Retinal Disease - затрагивает чуть более спорный подход к применению синтетических данных в медицине. Исследование "SynthEye" направлено на оценку потенциала улучшения ИИ в диагностике наследственных заболеваний сетчатки глаза (IRD) с использованием синтетических данных.

  Многие врачи относятся к генерации медицинских изображений с определенным скепсисом, опасаясь, что созданные искусственным интеллектом изображения могут не соответствовать физиологическим особенностям человеческого состояния или анатомии. Однако, существует проблема неравномерности классов в медицинских данных, которая может приводить к предвзятости моделей предсказания. Проблему надо решать.

![Канал нужно завалить камнем. Камень я не дам.](<img src="https://kartinkof.club/uploads/posts/2022-03/1648208846_1-kartinkof-club-p-kamen-ya-ne-dam-mem-1.jpg" width="50%" height="50%">)

  Для решения этой проблемы авторы применили генеративные противоборствующие сети (GANs), чтобы создать визуально правдоподобные синтетические изображения, имитирующие различные наследственные заболевания глаза. Однако, несмотря на высокую степень визуальной правдоподобности, синтетическое дополнение данных не привело к существенным улучшениям в классификации болезней.

Методы, описанные в статье:
- Обучение модели StyleGAN2 на реальных изображениях IRD для генерации синтетических изображений.
- Обучение сверточных нейронных сетей для классификации различных наборов данных, включая реальные и синтетические изображения.
- Сравнение производительности моделей с использованием реальных и синтетических данных.

Результаты:
- Синтетические изображения IRD, созданные с использованием SynthEye, обладали высокой степенью визуальной правдоподобности, хотя с общим качеством ниже (по сравнению с реальными изображениями).
- Модели, обученные только на синтетических данных, показали схожую производительность с моделями, обученными на реальных данных.
- Визуальный Тьюринг-тест с участием офтальмологов показал, что 47% синтетических изображений были неверно распознаны как реальные.

![Synthetic images produced by StyleGAN2](https://ars.els-cdn.com/content/image/1-s2.0-S2666914522001476-gr3.jpg)

  Эксперименты с различными наборами данных показали, что синтетическое дополнение не привело к улучшению производительности моделей, несмотря на успешную генерацию реалистичных изображений. Таким образом, синтетические данные, могут быть полезны для решения проблемы дисбаланса классов.
  
![Дисбаланс](https://cs14.pikabu.ru/images/big_size_comm/2023-03_2/167818100017745353.jpg)
