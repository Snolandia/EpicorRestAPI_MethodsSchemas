import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.InventoryAttributeSearchSvc
// Description: Service to search attribute sets and part bin if qualified
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InventoryAttributeSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InventoryAttributeSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InventoryAttributeSearchListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: This service will return all attribute sets based on AttrClassID and joining PartBin.
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (InventoryAttributeSearch) we need our own public method.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDynAttrValueSet:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: This service will return all attributes sets based on AttrClassID and attribute values
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (InventoryAttributeSearchList) we need our own public method.
   OperationID: Get_GetList
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClauseDynAttrValueSet:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListWithAttributeList
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetListWithAttributeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListWithAttributeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithAttributeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListWithAttributeList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetListWithAttributeList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForLotTracker
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetListForLotTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForLotTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetListForLotTracker", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsPartLotDynAttrValueSetView
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetRowsPartLotDynAttrValueSetView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPartLotDynAttrValueSetView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPartLotDynAttrValueSetView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsPartLotDynAttrValueSetView(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetRowsPartLotDynAttrValueSetView", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAttrClassID
   Description: Returns AttrClassID for a Part
   OperationID: GetAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttrClassID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/GetAttrClassID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InventoryAttributeSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InventoryAttributeSearchListRow[],
}

export interface Erp_Tablesets_InventoryAttributeSearchListRow{
      /**  ID of parent Attribute Class.  */  
   "AttrClassID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Company identifier.  */  
   "Company":string,
      /**  Description of attribute set.  */  
   "Description":string,
      /**  Short Decription of attribute set.  */  
   "ShortDescription":string,
   "PlanningAttributeSetSeq":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_InventoryAttributeSearchListRow{
      /**  ID of parent Attribute Class.  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Company identifier.  */  
   Company:string,
      /**  Description of attribute set.  */  
   Description:string,
      /**  Short Decription of attribute set.  */  
   ShortDescription:string,
   PlanningAttributeSetSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryAttributeSearchListTableset{
   InventoryAttributeSearchList:Erp_Tablesets_InventoryAttributeSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InventoryAttributeSearchRow{
      /**  ID of parent Attribute Class.  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Company identifier.  */  
   Company:string,
      /**  Description of attribute set.  */  
   Description:string,
      /**  Short Decription of attribute set.  */  
   ShortDescription:string,
      /**  The unique identifier of the Dynamic Attribute Planning Set.  */  
   PlanningAttributeSetSeq:number,
      /**  Total on hand qty for a specific part/lot  */  
   OnHandQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryAttributeSearchTableset{
   InventoryAttributeSearch:Erp_Tablesets_InventoryAttributeSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param company
      @param partNum
   */  
export interface GetAttrClassID_input{
   company:string,
   partNum:string,
}

export interface GetAttrClassID_output{
   returnObj:string,
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param attrClassID
      @param attributeListString
      @param pageSize
      @param absolutePage
   */  
export interface GetListForLotTracker_input{
   whereClauseDynAttrValueSet:string,
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListForLotTracker_output{
   returnObj:Erp_Tablesets_InventoryAttributeSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param attrClassID
      @param attributeListString
      @param pageSize
      @param absolutePage
   */  
export interface GetListWithAttributeList_input{
   whereClauseDynAttrValueSet:string,
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListWithAttributeList_output{
   returnObj:Erp_Tablesets_InventoryAttributeSearchListTableset[],
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
export interface GetList_input{
   whereClauseDynAttrValueSet:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_InventoryAttributeSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseDynAttrValueSet
      @param attrClassID
      @param attributeListString
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsPartLotDynAttrValueSetView_input{
   whereClauseDynAttrValueSet:string,
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsPartLotDynAttrValueSetView_output{
   returnObj:Erp_Tablesets_InventoryAttributeSearchTableset[],
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
   returnObj:Erp_Tablesets_InventoryAttributeSearchTableset[],
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

