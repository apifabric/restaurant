import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {RESTAURANTTABLE_MODULE_DECLARATIONS, RestaurantTableRoutingModule} from  './RestaurantTable-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    RestaurantTableRoutingModule
  ],
  declarations: RESTAURANTTABLE_MODULE_DECLARATIONS,
  exports: RESTAURANTTABLE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class RestaurantTableModule { }