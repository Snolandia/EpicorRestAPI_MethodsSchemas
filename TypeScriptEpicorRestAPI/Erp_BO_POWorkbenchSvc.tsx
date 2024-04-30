import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.POWorkbenchSvc
// Description: Purchase Part Multi UOM Planning Workbench Business Object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method CustomGetByID
   Description: Validates Part and returns a dataset including POWPart, UOMTotals, POWorkbenchMatrix and associated metadata
   OperationID: CustomGetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetByID(requestBody:CustomGetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomGetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/CustomGetByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CustomGetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOnHandQty
   Description: Get the total quantity we have in stock of this part converted
to the parts primary inventory UOM.
   OperationID: GetOnHandQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOnHandQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOnHandQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOnHandQty(requestBody:GetOnHandQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOnHandQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/GetOnHandQty", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOnHandQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOWorkbench
   Description: Retrieves data for UOM codes per part that are defined to be tracked for
it (PartUOM.TrackOnHand = true).
Part:         Only Parts where Part.TrackDimension is true should be used.
Horizon Date: Default to today.
If the date entered is before the current date an error message should appear.
This date will be used to limit the supply/demand displayed in the workbench.
Anything after the horizon date will be ignored.
   OperationID: GetPOWorkbench
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPOWorkbench_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOWorkbench_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOWorkbench(requestBody:GetPOWorkbench_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOWorkbench_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POWorkbenchSvc/GetPOWorkbench", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPOWorkbench_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
      @param horizonDate
      @param metadata
   */  
export interface CustomGetByID_input{
   partNum:string,
   horizonDate:string,
   metadata:Erp_Tablesets_DynamicMetadataTableset[],
}

export interface CustomGetByID_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   metadata:Erp_Tablesets_DynamicMetadataTableset,
}
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POWPartRow{
      /**  Part Number.  Only parts tracked in multiple UOM’s should be allowed.  If a part is entered that is not tracked in multiple’s, an error will be displayed.  */  
   PartNum:string,
      /**  Part description  */  
   PartDescription:string,
      /**  This is the total quantity we have in stock of this part converted to the parts primary inventory UOM.  */  
   OnHandQty:number,
      /**  The parts primary inventory UOM  */  
   IUM:string,
      /**  Default to today’s date.  Date entered must be greater than or equal to today’s date.  We should not allow past dates.  */  
   HorizonDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POWorkbenchRow{
      /**  Internal identifier for table that will tie multiple UOM for the same Date/Source together.  */  
   SortNum:number,
      /**  Date of the supply or demand  */  
   SourceDate:string,
      /**  Description of the supply or demand.  */  
   Source:string,
      /**  Base Unit of Measure for the Part.  Will be used to create the titles of UOM columns.  */  
   UOMCode:string,
      /**  The amount of the demand in base UOM  */  
   Inv_Demand:number,
      /**  The amount of the supply in base UOM  */  
   Inv_Supply:number,
      /**  The current inventory balance in base UOM  */  
   Inv_Balance:number,
      /**  The inventory amount in the specified UOM  */  
   UOM_Available:number,
      /**  The amount of the demand in the specified UOM if this is the UOM of the demand.  Otherwise will be 0.  */  
   UOM_Demand:number,
      /**  The amount of the supply in the specified UOM if this is the UOM of the supply.  Otherwise will be 0.  */  
   UOM_Supply:number,
      /**  The inventory amount in the specified UOM  */  
   UOM_Balance:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POWorkbenchTableset{
   POWorkbench:Erp_Tablesets_POWorkbenchRow[],
   POWPart:Erp_Tablesets_POWPartRow[],
   UOMTotals:Erp_Tablesets_UOMTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UOMTotalsRow{
      /**  Base Unit of Measure for the Part.  */  
   UOMCode:string,
      /**  Value used to convert to/from base uom for the specific part. Cannot change if it's base uom of UOMClass (always 1.0) Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions. For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table. When ConvOperator = * then ConvFactor is 1 UOM expressed in Base UOM else it is 1 Base UOM expressed in UOM  */  
   ConvFactor:number,
      /**  Amount in this UOM that is on hand  */  
   OnHandQty:number,
      /**  Amount in this UOM that is needed  */  
   RequiredQty:number,
      /**  Balance calculated by taking the Primary IUM Onhand qty and subtracting the demand qty and adding the demand qty (only if stock transaction, it will not be changed by non-stock transactions).  */  
   UOMOnHandQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface GetOnHandQty_input{
      /**  Part Number  */  
   ipPartNum:string,
}

export interface GetOnHandQty_output{
parameters : {
      /**  output parameters  */  
   opOnHandQty:number,
}
}

   /** Required : 
      @param ipPartNum
      @param ipHorizonDate
   */  
export interface GetPOWorkbench_input{
      /**  Part Number  */  
   ipPartNum:string,
      /**  Horizon Date  */  
   ipHorizonDate:string,
}

export interface GetPOWorkbench_output{
   returnObj:Erp_Tablesets_POWorkbenchTableset[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

