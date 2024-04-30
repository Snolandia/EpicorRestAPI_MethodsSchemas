import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMPlantSvc
// Description: Outbound integration point for Plant (Site)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata", {
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
   Summary: Invoke method AckSite
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckSite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AckSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckSite(requestBody:AckSite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AckSite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/AckSite", {
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
         resolve(data as AckSite_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CountSite
   Description: Returns the count of existing IntQueOut records along with the count of updated sites in the database that IntQueOut records have not yet been created for
   OperationID: CountSite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CountSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountSite(requestBody:CountSite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CountSite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/CountSite", {
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
         resolve(data as CountSite_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllSite
   Description: Generates IntQueOut and IMSite rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllSite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllSite(requestBody:GetAllSite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllSite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/GetAllSite", {
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
         resolve(data as GetAllSite_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSite
   Description: Generates IntQueOut and IMSite rows since the last time this was called and then returns these along with any existing
   OperationID: GetSite
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSite(requestBody:GetSite_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSite_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/GetSite", {
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
         resolve(data as GetSite_output)
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
      @param IMPlantTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckSite_input{
   IMPlantTableset:Erp_Tablesets_IMPlantTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckSite_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface CountSite_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountSite_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMPlantRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name. Used on shipping reports.  */  
   Name:string,
      /**  Site address line 1.  */  
   Address1:string,
      /**  Site address line 2.  */  
   Address2:string,
      /**  Site address line 3.  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Main phone number of the Site.  */  
   PhoneNum:string,
      /**  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  */  
   CommentText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  */  
   MaxLateDaysPORel:number,
      /**  Determines if the Plant has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMPlantTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMPlant:Erp_Tablesets_IMPlantRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
export interface GetAllSite_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllSite_output{
   returnObj:Erp_Tablesets_IMPlantTableset[],
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
export interface GetSite_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetSite_output{
   returnObj:Erp_Tablesets_IMPlantTableset[],
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

