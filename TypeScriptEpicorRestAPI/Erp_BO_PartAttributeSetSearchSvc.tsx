import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartAttributeSetSearchSvc
// Description: Service to Part with Attribute Set
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/$metadata", {
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttributeSetSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttributeSetSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttributeSetSearchListRow)
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
   Summary: Invoke method GetRows
   Description: This service is currently not implemented.
   OperationID: GetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows(requestBody:GetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/GetRows", {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: This service will return all parts and related attribute sets (if any).
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (PartAttributeSetSearch) we need our own public method.
   OperationID: GetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:GetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/GetList", {
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
         resolve(data as GetList_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttributeSetSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAttributeSetSearchListRow,
}

export interface Erp_Tablesets_PartAttributeSetSearchListRow{
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Inventory class that this Part belongs to.  */  
   "ClassID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Full Description of the Attribute Set.  */  
   "Description":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Product Group ID for the Part.  */  
   "ProdCode":string,
      /**  Indicates a Quantity Bearing part.  */  
   "QtyBearing":boolean,
      /**  The Short Description of the Attribute Set.  */  
   "ShortDescription":string,
      /**  Indicates if inventory for this part is tracked at the attribute level.  */  
   "TrackInventoryAttributes":boolean,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  */  
   "TypeCode":string,
      /**  Primary Inventory Unit of Measure.  */  
   "IUM":string,
      /**  A flag which indicates if this Part is not a stocked inventory item.  */  
   "NonStock":boolean,
      /**  Flag which indicates if the Part Master is considered as "Inactive".  */  
   "InActive":boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  */  
   "Method":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  An abbreviated part description field by which the user can search the Part file.  */  
   "SearchWord":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PartAttributeSetSearchListRow{
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Inventory class that this Part belongs to.  */  
   ClassID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  The Full Description of the Attribute Set.  */  
   Description:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Product Group ID for the Part.  */  
   ProdCode:string,
      /**  Indicates a Quantity Bearing part.  */  
   QtyBearing:boolean,
      /**  The Short Description of the Attribute Set.  */  
   ShortDescription:string,
      /**  Indicates if inventory for this part is tracked at the attribute level.  */  
   TrackInventoryAttributes:boolean,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  */  
   TypeCode:string,
      /**  Primary Inventory Unit of Measure.  */  
   IUM:string,
      /**  A flag which indicates if this Part is not a stocked inventory item.  */  
   NonStock:boolean,
      /**  Flag which indicates if the Part Master is considered as "Inactive".  */  
   InActive:boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  */  
   Method:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  An abbreviated part description field by which the user can search the Part file.  */  
   SearchWord:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAttributeSetSearchListTableset{
   PartAttributeSetSearchList:Erp_Tablesets_PartAttributeSetSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAttributeSetSearchRow{
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Inventory class that this Part belongs to.  */  
   ClassID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  The Full Description of the Attribute Set.  */  
   Description:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Product Group ID for the Part.  */  
   ProdCode:string,
      /**  Indicates a Quantity Bearing part.  */  
   QtyBearing:boolean,
      /**  The Short Description of the Attribute Set.  */  
   ShortDescription:string,
      /**  Indicates if inventory for this part is tracked at the attribute level.  */  
   TrackInventoryAttributes:boolean,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item.  */  
   NonStock:boolean,
      /**  Flag which indicates if the Part Master is considered as "Inactive".  */  
   InActive:boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  */  
   Method:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Primary Inventory Unit of Measure.  */  
   IUM:string,
      /**  An abbreviated part description field by which the user can search the Part file.  */  
   SearchWord:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAttributeSetSearchTableset{
   PartAttributeSetSearch:Erp_Tablesets_PartAttributeSetSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
   whereClauseDynAttrValueSet:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PartAttributeSetSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynAttrValueSet:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartAttributeSetSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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

