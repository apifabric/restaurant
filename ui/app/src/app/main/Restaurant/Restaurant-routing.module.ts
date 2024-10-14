import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RestaurantHomeComponent } from './home/Restaurant-home.component';
import { RestaurantNewComponent } from './new/Restaurant-new.component';
import { RestaurantDetailComponent } from './detail/Restaurant-detail.component';

const routes: Routes = [
  {path: '', component: RestaurantHomeComponent},
  { path: 'new', component: RestaurantNewComponent },
  { path: ':id', component: RestaurantDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Restaurant-detail-permissions'
      }
    }
  },{
    path: ':restaurant_id/Chef', loadChildren: () => import('../Chef/Chef.module').then(m => m.ChefModule),
    data: {
        oPermission: {
            permissionId: 'Chef-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/Inventory', loadChildren: () => import('../Inventory/Inventory.module').then(m => m.InventoryModule),
    data: {
        oPermission: {
            permissionId: 'Inventory-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/Menu', loadChildren: () => import('../Menu/Menu.module').then(m => m.MenuModule),
    data: {
        oPermission: {
            permissionId: 'Menu-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/Reservation', loadChildren: () => import('../Reservation/Reservation.module').then(m => m.ReservationModule),
    data: {
        oPermission: {
            permissionId: 'Reservation-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/RestaurantTable', loadChildren: () => import('../RestaurantTable/RestaurantTable.module').then(m => m.RestaurantTableModule),
    data: {
        oPermission: {
            permissionId: 'RestaurantTable-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/Review', loadChildren: () => import('../Review/Review.module').then(m => m.ReviewModule),
    data: {
        oPermission: {
            permissionId: 'Review-detail-permissions'
        }
    }
}
];

export const RESTAURANT_MODULE_DECLARATIONS = [
    RestaurantHomeComponent,
    RestaurantNewComponent,
    RestaurantDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RestaurantRoutingModule { }