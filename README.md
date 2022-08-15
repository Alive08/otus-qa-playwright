# otus-qa-playwright

Playwright UI tests for Opencart (proof of concept)

Опции запуска (помимо стандартных рпций pytest'а):
    --browser [chromium] - используемый браузер (chromium, firefox, webkit)
    --headed [false] - запускать браузер в "headed" режиме (с отображением)
    --base-usl - базовый URL тестируемого веб-приложения
    --db-host [localhost] - адрес сервера MySQL
    --test-log-level [INFO] - уровень логгирования ("DEBUG", "INFO", "WARNING", "ERROR")
    --test-log-file [artifacts/testrun.log] - путь к лог-файлу
    --screenshots-dir [artifacts/screenshots] - путь к каталогу скриншотов

Тесты можно запустить:

- локально на хосте из каталога проекта:
    pytest <опции запуска> <тесты>
    ,при этом предварительно должно быть запущено приложение opencart. Его можно запустить так:
    
    cd environment/opencart
    ./up.sh
    
    после прогона тестов приложение можно остановить из того же каталога
    
    cd environment/opencart
    ./down.sh
    
    Также можно воспользоваться скриптом
    run_tests_local.sh <опции запуска> <тесты>

- в докере с использованием docker-compose. Для этого удобно воспользоваться скриптом
    run_tests_compose.sh <опции запуска> <тесты>

- в CI Jenkins - пайплайн opencart_tests_pipeline_playwright с передачей требуемых параметров.
    пайплайн запускается полностью в докере. Пайплайн описан в файле jenkins/pipeline-docker/Jenkinsfile

В каждом случае можно задать переменную окружения DEBUG=pw:api, при этом производится расширенное логгирование
вызовов API Playwright, что упрощает отладку тестов.
