# Instrucciones de configuración y uso

## 1. Levantar los contenedores
Ejecuta el siguiente comando para iniciar los servicios definidos en el `docker-compose.yml`:

    docker compose up -d

## 2. Acceder a Odoo
Una vez que los contenedores estén arriba, abre la siguiente URL en tu navegador:

http://localhost:8015

Accede con las siguientes credenciales por defecto:
- Usuario: admin
- Contraseña: admin

## 3. Activar módulos necesarios
1. Dirígete al apartado **Apps**.
2. Busca **Purchase Order** y actívalo.

Nota: al instalarlo también se instalará automáticamente la app **Purchase**, ya que es requerida.

## 4. Configuración de usuarios
1. Ve a **Settings > Manage Users**.
2. Ingresa al usuario **Administrador**.
3. Dentro del apartado **Category**, asigna el rol **Categorizar Compra**.
   Esto permitirá crear categorías y asignarlas posteriormente a cualquier usuario.

## 5. Crear categorías
1. Ve al módulo **Purchase**.
2. Recarga la página en el navegador.
3. Verás un nuevo submenú llamado **Category**.
4. Desde ahí podrás crear nuevas categorías con su nombre y descripción.

## 6. Asignar categorías a usuarios
1. Al crear o editar un usuario, verás dos nuevos campos:
   - Category: aquí selecciona la opción "Categorizar Compra".
   - Categorías de compra: selecciona las categorías creadas anteriormente.

De esta forma, cada usuario podrá visualizar únicamente las órdenes de compra que pertenezcan a las categorías asignadas.

## 7. Asignar categorías a órdenes de compra
- Al crear una nueva orden, el campo **Categoría de Compra** solo estará disponible cuando la orden esté en el estado **Purchase**.
- Una vez en este estado, podrás asignarle una categoría.
- El usuario solo podrá ver la orden si tiene asignada la misma categoría.

## nota:
-- al asignar una categoria a una orden y el usuario no pertenece y quieres cambiarlo de nuevo, como se guarda automaticamente y ya no me pertenece puede que lance un error: 
Access Error
Due to security restrictions, you are not allowed to access 'Purchase Order' (purchase.order) records.
Contact your administrator to request access if necessary.
-pero la orden si se guardo
