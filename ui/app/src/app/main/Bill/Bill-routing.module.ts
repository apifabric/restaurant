import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BillHomeComponent } from './home/Bill-home.component';
import { BillNewComponent } from './new/Bill-new.component';
import { BillDetailComponent } from './detail/Bill-detail.component';

const routes: Routes = [
  {path: '', component: BillHomeComponent},
  { path: 'new', component: BillNewComponent },
  { path: ':id', component: BillDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Bill-detail-permissions'
      }
    }
  }
];

export const BILL_MODULE_DECLARATIONS = [
    BillHomeComponent,
    BillNewComponent,
    BillDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BillRoutingModule { }