import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MobileCRMSvc
// Description: MobileCRM main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata", {
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



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetCRMEnvironment
   Description: Get CRM Environment Variables
   OperationID: GetCRMEnvironment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMEnvironment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCRMEnvironment(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/GetCRMEnvironment", {
          method: 'post',
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
   Summary: Invoke method SetCustomerIndustryCodes
   Description: Set customer Industry Types
   OperationID: SetCustomerIndustryCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCustomerIndustryCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCustomerIndustryCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCustomerIndustryCodes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/SetCustomerIndustryCodes", {
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
   Summary: Invoke method SetCustomerAttributes
   Description: Set Customer Attributes
   OperationID: SetCustomerAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCustomerAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCustomerAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCustomerAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/SetCustomerAttributes", {
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
   Summary: Invoke method CreatePerConLink
   Description: Create PerConLnk records. Pass only the perConLnk table
   OperationID: CreatePerConLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePerConLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePerConLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePerConLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/CreatePerConLink", {
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



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param perCon
   */  
export interface CreatePerConLink_input{
   perCon:Erp_Tablesets_CRMPerConLnkListTableset[],
}

export interface CreatePerConLink_output{
}

export interface Erp_Tablesets_AttributListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies an attribute master record.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   AttrCode:string,
      /**  Description of the attribute  */  
   AttrDescription:string,
      /**  Determines whether or not this attribute can be assigned to a customer.  */  
   Inactive:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AttributListTableset{
   AttributList:Erp_Tablesets_AttributListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CRMEnvironmentDataTableset{
   CRMEnvironment:Erp_Tablesets_CRMEnvironmentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CRMEnvironmentRow{
   UserID:string,
      /**  Server local time  */  
   ServerTime:string,
   ServerUtcTime:string,
   ServerUtcOffset:number,
   TenantID:string,
   PatchLevel:string,
   PatchLevelApp:string,
   InstallationName:string,
   CurLangID:string,
   CountryCode:string,
   ClientDateFormat:string,
   ProductName:string,
   ProductCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRMPerConLnkListTableset{
   CRMPerConLnk:Erp_Tablesets_CRMPerConLnkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CRMPerConLnkRow{
   PerConID:number,
   ContextLink:string,
   LinkSysRowID:string,
   PrimaryContext:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ICCodeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Represents the SIC/ISIC/NAICS/NACE code for the current industry class.  */  
   ICCode:string,
      /**  Foreign key to ICType table. A short name, acronym or identifier for the Industry Class Type.  */  
   ICTypeID:string,
      /**  Descriptive name for the Industry Class.  */  
   Description:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   ICTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ICTypeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A short name, acronym or identifier for the Industry Class Type.  */  
   ICTypeID:string,
      /**  Full name or description for the Industry Class Type.  */  
   Description:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IndustryClassTableset{
   ICType:Erp_Tablesets_ICTypeRow[],
   ICCode:Erp_Tablesets_ICCodeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetCRMEnvironment_output{
   returnObj:Erp_Tablesets_CRMEnvironmentDataTableset[],
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
      @param customerNumber
      @param attributeList
   */  
export interface SetCustomerAttributes_input{
      /**  Customer Number  */  
   customerNumber:number,
   attributeList:Erp_Tablesets_AttributListTableset[],
}

export interface SetCustomerAttributes_output{
}

   /** Required : 
      @param customerNumber
      @param deleteNonListed
      @param industryCodeList
   */  
export interface SetCustomerIndustryCodes_input{
      /**  Customer Number  */  
   customerNumber:number,
      /**  True to Delete any ietms not listed  */  
   deleteNonListed:boolean,
   industryCodeList:Erp_Tablesets_IndustryClassTableset[],
}

export interface SetCustomerIndustryCodes_output{
}

