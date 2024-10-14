import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Bill', loadChildren: () => import('./Bill/Bill.module').then(m => m.BillModule) },
    
        { path: 'Chef', loadChildren: () => import('./Chef/Chef.module').then(m => m.ChefModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Ingredient', loadChildren: () => import('./Ingredient/Ingredient.module').then(m => m.IngredientModule) },
    
        { path: 'Inventory', loadChildren: () => import('./Inventory/Inventory.module').then(m => m.InventoryModule) },
    
        { path: 'Menu', loadChildren: () => import('./Menu/Menu.module').then(m => m.MenuModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'Reservation', loadChildren: () => import('./Reservation/Reservation.module').then(m => m.ReservationModule) },
    
        { path: 'Restaurant', loadChildren: () => import('./Restaurant/Restaurant.module').then(m => m.RestaurantModule) },
    
        { path: 'RestaurantTable', loadChildren: () => import('./RestaurantTable/RestaurantTable.module').then(m => m.RestaurantTableModule) },
    
        { path: 'Review', loadChildren: () => import('./Review/Review.module').then(m => m.ReviewModule) },
    
        { path: 'SupplyOrder', loadChildren: () => import('./SupplyOrder/SupplyOrder.module').then(m => m.SupplyOrderModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }