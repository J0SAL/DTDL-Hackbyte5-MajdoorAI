mermaid_prompts = {
    "flowchart": {
        "name": "Flowchart",
        "code": '''graph TD;
            A[Start] --> B[Process 1];
            B --> C[Process 2];
            C --> D[Process 3];
            D --> E[End];''',
    },
    "sequenc_diagram": {
        "name": "Sequence Diagram",
        "code": '''sequenceDiagram
        Alice->>John: Hello John, how are you?
        John-->>Alice: Great!
        Alice-)John: See you later!''',
    },
    "class_diagram": {
    "name": "Class Diagram",
    "code": '''classDiagram
        note "From Duck till Zebra"
        Animal <|-- Duck
        note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
        Animal <|-- Fish
        Animal <|-- Zebra
        Animal : +int age
        Animal : +String gender
        Animal: +isMammal()
        Animal: +mate()
        class Duck{
            +String beakColor
            +swim()
            +quack()
        }
        class Fish{
            -int sizeInFeet
            -canEat()
        }
        class Zebra{
            +bool is_wild
            +run()
        }''',
    },
    "er_diagram": {
        "name": "ER Diagram",
        "code": '''erDiagram
            CUSTOMER ||--o{ ORDER : places
            CUSTOMER {
                string name
                string custNumber
                string sector
            }
            ORDER ||--|{ LINE-ITEM : contains
            ORDER {
                int orderNumber
                string deliveryAddress
            }
            LINE-ITEM {
                string productCode
                int quantity
                float pricePerUnit
            }
        ''',
    },
    "block_diagram": {
        "name": "Block Diagram",
        "code": '''block-beta
        columns 1
        db(("DB"))
        blockArrowId6<["&nbsp;&nbsp;&nbsp;"]>(down)
        block:ID
            A
            B["A wide one in the middle"]
            C
        end
        space
        D
        ID --> D
        C --> D
        style B fill:#969,stroke:#333,stroke-width:4px''',
    },
}