import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMABCCodeSvc
// Description: Business Object to handle: Count, Get, Ack, Add, Update and Delete of ABCCode
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", {
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
   Summary: Invoke method AckABCCode
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AckABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckABCCode(requestBody:AckABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AckABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/AckABCCode", {
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
         resolve(data as AckABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CountABCCode
   Description: Returns the count of existing IntQueOut records along with the count of updated abcCodes in the database that IntQueOut records have not yet been created for
   OperationID: CountABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CountABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountABCCode(requestBody:CountABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CountABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/CountABCCode", {
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
         resolve(data as CountABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllABCCode
   Description: Generates IntQueOut and IMABCCode rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllABCCode(requestBody:GetAllABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/GetAllABCCode", {
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
         resolve(data as GetAllABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetABCCode
   Description: Generates IntQueOut and IMABCCode rows since the last time this was called and then returns these along with any existing
   OperationID: GetABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetABCCode(requestBody:GetABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/GetABCCode", {
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
         resolve(data as GetABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddABCCode
   Description: Add ABCCode
   OperationID: AddABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddABCCode(requestBody:AddABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/AddABCCode", {
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
         resolve(data as AddABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteABCCode
   Description: Delete ABCCode
   OperationID: DeleteABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteABCCode(requestBody:DeleteABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/DeleteABCCode", {
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
         resolve(data as DeleteABCCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateABCCode
   Description: Update ABCCode
   OperationID: UpdateABCCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateABCCode(requestBody:UpdateABCCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateABCCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/UpdateABCCode", {
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
         resolve(data as UpdateABCCode_output)
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
      @param IMABCCodeTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckABCCode_input{
   IMABCCodeTableset:Erp_Tablesets_IMABCCodeTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckABCCode_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param IMABCCodeTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddABCCode_input{
   IMABCCodeTableset:Erp_Tablesets_IMABCCodeTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddABCCode_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface CountABCCode_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountABCCode_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

   /** Required : 
      @param IMABCCodeTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface DeleteABCCode_input{
   IMABCCodeTableset:Erp_Tablesets_IMABCCodeTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface DeleteABCCode_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

export interface Erp_Tablesets_IMABCCodeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  Indicates how often parts in the classification are to be counted expressed in number of days  */  
   CountFreq:number,
      /**  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in SiteConfABC and/or WarehseABC.  */  
   ExcludeFromCC:boolean,
      /**  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in SiteConfABC and/or WarehseABC.  */  
   StockValPcnt:number,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC. Zero indicates that any quantity variance is considered out  */  
   PcntTolerance:number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcPcnt:boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcQty:boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcValue:boolean,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC. Zero indicates that any quantity variance is consid  */  
   QtyTolerance:number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  */  
   ValueTolerance:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMABCCodeTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMABCCode:Erp_Tablesets_IMABCCodeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMIntegrationKeyRow{
      /**  The master file which the integration is related to.  */  
   TableName:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMIntegrationKeyTableset{
   IMIntegrationKey:Erp_Tablesets_IMIntegrationKeyRow[],
   IMNaturalKeys:Erp_Tablesets_IMNaturalKeysRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMNaturalKeysRow{
   KeyValue:string,
   KeyColumn:string,
   Sequence:number,
   PrimaryKey:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntQueInOutRow{
      /**  The unique key from IntQueIn or IntQueOut  */  
   IntQueID:number,
      /**  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  */  
   Action:string,
      /**  "I" for incoming or "O" for outgoing  */  
   IncomingOutgoing:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetABCCode_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetABCCode_output{
   returnObj:Erp_Tablesets_IMABCCodeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetAllABCCode_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllABCCode_output{
   returnObj:Erp_Tablesets_IMABCCodeTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param IMABCCodeTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface UpdateABCCode_input{
   IMABCCodeTableset:Erp_Tablesets_IMABCCodeTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface UpdateABCCode_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

