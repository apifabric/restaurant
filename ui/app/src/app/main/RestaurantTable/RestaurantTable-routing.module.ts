import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RestaurantTableHomeComponent } from './home/RestaurantTable-home.component';
import { RestaurantTableNewComponent } from './new/RestaurantTable-new.component';
import { RestaurantTableDetailComponent } from './detail/RestaurantTable-detail.component';

const routes: Routes = [
  {path: '', component: RestaurantTableHomeComponent},
  { path: 'new', component: RestaurantTableNewComponent },
  { path: ':id', component: RestaurantTableDetailComponent,
    data: {
      oPermission: {
        permissionId: 'RestaurantTable-detail-permissions'
      }
    }
  }
];

export const RESTAURANTTABLE_MODULE_DECLARATIONS = [
    RestaurantTableHomeComponent,
    RestaurantTableNewComponent,
    RestaurantTableDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RestaurantTableRoutingModule { }