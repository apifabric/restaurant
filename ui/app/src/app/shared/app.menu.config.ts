import { MenuRootItem } from 'ontimize-web-ngx';

import { BillCardComponent } from './Bill-card/Bill-card.component';

import { ChefCardComponent } from './Chef-card/Chef-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { IngredientCardComponent } from './Ingredient-card/Ingredient-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { MenuCardComponent } from './Menu-card/Menu-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { ReservationCardComponent } from './Reservation-card/Reservation-card.component';

import { RestaurantCardComponent } from './Restaurant-card/Restaurant-card.component';

import { RestaurantTableCardComponent } from './RestaurantTable-card/RestaurantTable-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SupplyOrderCardComponent } from './SupplyOrder-card/SupplyOrder-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Bill', name: 'BILL', icon: 'view_list', route: '/main/Bill' }
    
        ,{ id: 'Chef', name: 'CHEF', icon: 'view_list', route: '/main/Chef' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Ingredient', name: 'INGREDIENT', icon: 'view_list', route: '/main/Ingredient' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Menu', name: 'MENU', icon: 'view_list', route: '/main/Menu' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'Reservation', name: 'RESERVATION', icon: 'view_list', route: '/main/Reservation' }
    
        ,{ id: 'Restaurant', name: 'RESTAURANT', icon: 'view_list', route: '/main/Restaurant' }
    
        ,{ id: 'RestaurantTable', name: 'RESTAURANTTABLE', icon: 'view_list', route: '/main/RestaurantTable' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'SupplyOrder', name: 'SUPPLYORDER', icon: 'view_list', route: '/main/SupplyOrder' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    BillCardComponent

    ,ChefCardComponent

    ,CustomerCardComponent

    ,IngredientCardComponent

    ,InventoryCardComponent

    ,MenuCardComponent

    ,OrderCardComponent

    ,ReservationCardComponent

    ,RestaurantCardComponent

    ,RestaurantTableCardComponent

    ,ReviewCardComponent

    ,SupplyOrderCardComponent

];