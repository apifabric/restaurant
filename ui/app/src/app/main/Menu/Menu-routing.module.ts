import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuHomeComponent } from './home/Menu-home.component';
import { MenuNewComponent } from './new/Menu-new.component';
import { MenuDetailComponent } from './detail/Menu-detail.component';

const routes: Routes = [
  {path: '', component: MenuHomeComponent},
  { path: 'new', component: MenuNewComponent },
  { path: ':id', component: MenuDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Menu-detail-permissions'
      }
    }
  }
];

export const MENU_MODULE_DECLARATIONS = [
    MenuHomeComponent,
    MenuNewComponent,
    MenuDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MenuRoutingModule { }