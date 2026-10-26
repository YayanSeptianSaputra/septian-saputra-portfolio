# ERD and UML: domain model of the SauceDemo shop

SauceDemo (saucedemo.com) is a public demo shop with no visible database. This is a **domain model I derived from its observable behaviour** (login, product list, cart, checkout), written the way I would document a system under test.

## 1. ERD

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER ||--o| CART : owns
    CART ||--o{ CART_ITEM : contains
    PRODUCT ||--o{ CART_ITEM : "is added as"
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "is ordered as"

    USER {
        int id PK
        string username UK
        string status "active or locked_out"
    }
    PRODUCT {
        int id PK
        string name
        string description
        decimal price
    }
    CART {
        int id PK
        int user_id FK
    }
    CART_ITEM {
        int id PK
        int cart_id FK
        int product_id FK
        int quantity
    }
    ORDER {
        int id PK
        int user_id FK
        string first_name
        string last_name
        string postal_code
        decimal item_total
        decimal tax
        decimal total
    }
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }
```

## 2. Use case (UML)

```mermaid
flowchart LR
    Shopper((Shopper))
    subgraph SauceDemo
        UC1[Log in]
        UC2[Browse and sort products]
        UC3[Add or remove cart items]
        UC4[Check out]
        UC5[Log out]
    end
    Shopper --> UC1
    Shopper --> UC2
    Shopper --> UC3
    Shopper --> UC4
    Shopper --> UC5
    UC2 -. requires .-> UC1
    UC4 -. includes .-> UC3
```

## 3. Sequence diagram (UML): checkout

```mermaid
sequenceDiagram
    actor S as Shopper
    participant UI as Web UI
    participant SV as Shop logic
    S->>UI: Click Checkout
    UI-->>S: Show information form
    S->>UI: Enter name and postal code, Continue
    UI->>SV: Validate required fields
    SV-->>UI: Valid
    UI-->>S: Overview with item total, tax, total
    S->>UI: Click Finish
    UI->>SV: Create order, clear cart
    SV-->>UI: Order confirmed
    UI-->>S: Thank you for your order
```

## 4. State diagram (UML): checkout

```mermaid
stateDiagram-v2
    [*] --> CartOpen
    CartOpen --> InformationStep: Checkout
    InformationStep --> OverviewStep: valid data
    InformationStep --> InformationStep: validation error
    InformationStep --> CartOpen: Cancel
    OverviewStep --> Complete: Finish
    OverviewStep --> CartOpen: Cancel
    Complete --> [*]
```

## 5. Class diagram (UML)

```mermaid
classDiagram
    class User { +string username +string status +login() +logout() }
    class Product { +string name +decimal price }
    class Cart { +add(product) +remove(product) +count() }
    class Order { +decimal itemTotal +decimal tax +decimal total +complete() }
    User "1" --> "0..1" Cart
    User "1" --> "0..*" Order
    Cart "1" o-- "0..*" Product
    Order "1" *-- "1..*" Product
```
