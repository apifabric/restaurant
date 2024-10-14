import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChefHomeComponent } from './home/Chef-home.component';
import { ChefNewComponent } from './new/Chef-new.component';
import { ChefDetailComponent } from './detail/Chef-detail.component';

const routes: Routes = [
  {path: '', component: ChefHomeComponent},
  { path: 'new', component: ChefNewComponent },
  { path: ':id', component: ChefDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Chef-detail-permissions'
      }
    }
  }
];

export const CHEF_MODULE_DECLARATIONS = [
    ChefHomeComponent,
    ChefNewComponent,
    ChefDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ChefRoutingModule { }