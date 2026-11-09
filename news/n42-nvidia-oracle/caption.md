Агент упирается не в GPU, а в то, что происходит между вызовами модели.

Nvidia и Oracle объявили: Vera Rubin NVL72 и Vera CPU теперь общедоступны на Oracle Cloud Infrastructure, Superclusters планируют расширить до мультигигаватт. Планируют HGX Rubin NVL8 — восемь GPU в x86-сервере.

Почему это важно: GPU считает модель, а CPU выполняет инструменты, тестирует код и достаёт данные. Если CPU медленный, дорогой GPU простаивает. OCI Kubernetes Engine позволяет масштабировать CPU и GPU независимо, а Oracle Acceleron даёт аппаратную изоляцию для недоверенного кода агента.

Пример: OpenAI обучала GPT-6 Astra на OCI с более чем 100 000 GPU Blackwell. Vera CPU она выводит в продакшен для agentic sandbox.

Что это значит для того, кто внедряет: мерить простой GPU, разделять CPU и GPU, изолировать код агента. Узкое место часто не модель, а то, что между вызовами (данные на 30.10.2026).

Ссылки:
пресс-релиз — nvidianews.nvidia.com/news/nvidia-and-oracle-expand-nvidia-vera-rubin-to-multi-gigawatt-scale-and-bring-nvidia-vera-cpu-to-oracle-cloud-infrastructure

Полный разбор со ссылками на первоисточники — в Telegram @pro_llm, ссылка в профиле.

#NVIDIA #Oracle #AIагенты #инфраструктура
