Итоговый проект.

Входная информация:

Компания получила заказ от Федерации спортивного туризма России (ФСТР).

ФСТР — организация, занимающаяся развитием и популяризацией спортивного туризма в России и осуществляющая надзор за проведением всероссийских соревнований по этому виду спорта.

Туристы будут пользоваться мобильным приложением. В горах они введут данные о пропуске в приложение и отправят их в МАГАЗИН, как только появится доступ в Интернет.

Модератор из федерации проверит и внесет в базу данных информацию, полученную от пользователей, а те, в свою очередь, смогут видеть статус модерации в мобильном приложении и просматривать базу данных с объектами, введенными другими пользователями.

Для получения выходной информации смотрите /swagger-ui/ или информацию ниже.

    openapi: 3.0.2
      info:
      title: 'Mountain pass'
      version: "0.1"

    paths:
      /SubmitData/:

    get:
      operationId: SubmitData
      description: 'List of perevals'
      parameters: [ ]
      responses:
        '200':
          content:
            application/json:
            schema:
              type: object
              items:
              $ref: '#/components/schemas/pereval'
          description: Success
      tags:
        - pereval

    post:
      operationId: SubmitData
      description: 'Create pereval'
      parameters: [ ]
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/pereval'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/pereval'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/pereval'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/pereval'
          description: Success'
        '405':
          description: Invalid input
        '400':
          description: Bad Request
        tags:
          - pereval

    /SubmitData/{id}/:
      get:
          operationId: SubmitData
          description: 'Get pereval by ID'
          parameters:
          - name: id
            in: path
            required: true
            schema:
              type: integer
          responses:
            '200' :
              $ref: '#/components/schemas/pereval'
              description: 'Success'
            '404':
              description: 'Not found'
              content:
                text/plain:
                  schema:
                    title: Not found
                    type: string
                    example: Not found
            '500':
              description: Invalid input
              content:
                application/json:
                  schema:
                    title: error
          tags:
            - pereval

    patch:
        operationId: SubmitData
        description: 'Partial update by ID'
        parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
        requestBody:
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/pereval'
            application/x-www-form-urlencoded:
              schema:
                $ref: '#/components/schemas/pereval'
            multipart/form-data:
              schema:
                $ref: '#/components/schemas/pereval'
        responses:
          '200' :
            $ref: '#/components/schemas/pereval'
            description: Success
          '404' :
            description: Not found
        tags:
        - pereval

    /SubmitData/?author__email={email}:
      get:
        description: SubmitData
        operationId: 'Search by email'
        parameters:
          - name: email
            in: path
            required: true
            schema:
              type: string
        responses:
          '200':
            content:
              application/json:
              schema:
                type: object
                items:
                $ref: '#/components/schemas/pereval'
            description: Success
        tags:
          - pereval
  
    components:
      schemas:
        pereval:
          type: object
          title: pereval
          description: Перевал
          properties:
            beautyTitle:
              type: string
              example: Перевал
            title:
              type: string
              example: Семинский перевал
            other_titles:
              type: string
              example: Самый высокий на Чуйсуком тракте
            connect:
              type: string
              example: Между Северным и Централиным Алтаем
            author:
              type: object
              $ref: '#/components/schemas/Author'
            coords:
              type: object
              $ref: '#/components/schemas/Coords'
            level:
              type: object
              $ref: '#/components/schemas/Level'
            add_time:
              type: string
              format: timezone
            image:
              type: array
              items:
                type: object
                $ref: '#/components/schemas/Image'
                example: [
                { "image_name": "перевал 1", "image": "https://www.nastol.com.ua/pic/201411/1280x1024/nastol.com.ua-116730.jpg" },
              ]
            status:
              type: string
              enum:
                  - NEW
                  - PEN
                  - ACC
                  - REJ
              default: NEW

    Author:
      type: object
      title: Author
      description: Автор
      properties:
        email:
          type: string
          example: Merk_94@mail.ru
        fam:
          type: string
          example: Пупкин
        name:
          type: string
          example: Вячеслав
        otc:
          type: string
          example: Пупкинович

        phone:
          type: string
          example: +79605558766


    Coords:
      type: object
      title: Coords
      description: Координаты
      properties:
        latitude:
          type: number
          example: 27.988056
        longitude:
          type: number
          example: 86.925278
        height:
          type: integer
          example: 8848

    Level:
      type: object
      title: Level
      description: Уровень сложности
      properties:
        winter:
          type: string
          enum:
            - NI
            - A1
            - B1
            - A2
            - B2
            - A3
            - B3
        summer:
          type: string
          enum:
            - NI
            - A1
            - B1
            - A2
            - B2
            - A3
            - B3
        autumn:
          type: string
          enum:
            - NI
            - A1
            - B1
            - A2
            - B2
            - A3
            - B3
        spring:
          type: string
          enum:
            - NI
            - A1
            - B1
            - A2
            - B2
            - A3
            - B3

    Image:
      type: object
      title: Images
      description: Фотография перевала
      properties:
        image_name:
          type: string
          example: Перевал
        image:
          type: string
          format: url
          description: Photo link
          example: https://www.nastol.com.ua/pic/201411/1280x1024/nastol.com.ua-116730.jpg