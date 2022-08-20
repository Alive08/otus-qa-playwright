# otus-qa-playwright

Playwright UI tests for Opencart (proof of concept)

Опции запуска (помимо стандартных аргументов pytest'а):
   - --browser [chromium] - используемый браузер (chromium, firefox, webkit)
   - --headed [false] - запускать браузер в "headed" режиме (с отображением)
   - --base-usl - базовый URL тестируемого веб-приложения
   - --db-host [localhost] - адрес сервера MySQL
   - --test-log-level [INFO] - уровень логгирования ("DEBUG", "INFO", "WARNING", "ERROR")
   - --test-log-file [artifacts/testrun.log] - путь к лог-файлу
   - --screenshots-dir [artifacts/screenshots] - путь к каталогу скриншотов

 Подготовить рабочее окружение можно при помощи скрипта

    ./setup-dev-env.sh

если установка прошла успешно, в результате выполнения команды

    playwright open http://otus.ru

в браузере будет открыта главная страница сайта otus.ru

если необходимо работать с движком webkit, нужно установить зависимости (требуется sudo):

    playwright install-deps

Для установки зависимостей playwright, возможно, придется выполнить команду:
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB3E94ADBE1229CF

Приведенные срипты содержат ссылки на доменное имя 'opencart', которое нужно внести в /etc/hosts
для правильной работы скриптов:

    <IP адрес вашего хоста> opencart, например
    192.168.117.131 opencart

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
    Также предусмотрен вариант запуска тестов непосредственно на хосте -
    пайплайн jenkins/pipeline-local/Jenkinsfile

В каждом случае можно задать переменную окружения DEBUG=pw:api, при этом производится расширенное
логгирование вызовов API Playwright, что упрощает отладку тестов.
