import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MESMenuSvc
// Description: Business object to interact with Handheld/MES Menu Security
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", {
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
   Summary: Invoke method CheckMESMenuInitializedStatus
   Description: Checks whether the current company has any MESMenu data initialized.
   OperationID: CheckMESMenuInitializedStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMESMenuInitializedStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckMESMenuInitializedStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/CheckMESMenuInitializedStatus", {
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
   Summary: Invoke method CheckCurrentUserSecurityMgr
   Description: Checks whether the current user is a security manager.
   OperationID: CheckCurrentUserSecurityMgr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrentUserSecurityMgr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCurrentUserSecurityMgr(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/CheckCurrentUserSecurityMgr", {
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
   Summary: Invoke method CheckEmployeeID
   Description: Checks whether the specified employee is a valid, active employee.
   OperationID: CheckEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEmployeeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/CheckEmployeeID", {
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
   Summary: Invoke method CheckUserSiteAccess
   Description: Checks whether the specified user has access to the site defined in MES.
   OperationID: CheckUserSiteAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUserSiteAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUserSiteAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckUserSiteAccess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/CheckUserSiteAccess", {
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
   Summary: Invoke method GetMenuData
   Description: Gets MESMenu data
   OperationID: GetMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMenuData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/GetMenuData", {
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
   Summary: Invoke method UpdateMenuData
   Description: Updates MESMenu and MESMenuSecurity tables
   OperationID: UpdateMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMenuData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/UpdateMenuData", {
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
   Summary: Invoke method InitializeMESMenu
   Description: Initializes or reinitializes the MESMenu data for the current company.
   OperationID: InitializeMESMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeMESMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeMESMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeMESMenu(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/InitializeMESMenu", {
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
   Summary: Invoke method SetEmployeeID
   Description: Call to change EmployeeID if allowed by EmpBasic settings
   OperationID: SetEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetEmployeeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/SetEmployeeID", {
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
   Summary: Invoke method ImportMESMenuData
   Description: Import MESMenu data received in a MESMenuTableset, and add it into MESMenu and MESMenuSecurity tables.
   OperationID: ImportMESMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportMESMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportMESMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportMESMenuData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/ImportMESMenuData", {
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
export interface CheckCurrentUserSecurityMgr_output{
parameters : {
      /**  output parameters  */  
   isSecurityMgr:boolean,
}
}

   /** Required : 
      @param empID
   */  
export interface CheckEmployeeID_input{
      /**  Employee ID to check  */  
   empID:string,
}

export interface CheckEmployeeID_output{
parameters : {
      /**  output parameters  */  
   sysUserID:string,
   empName:string,
   isValidActiveEmp:boolean,
}
}

export interface CheckMESMenuInitializedStatus_output{
parameters : {
      /**  output parameters  */  
   isInitialized:boolean,
}
}

   /** Required : 
      @param companyID
      @param userID
      @param newSite
   */  
export interface CheckUserSiteAccess_input{
      /**  Company ID defined in MES.  */  
   companyID:string,
      /**  User ID to check  */  
   userID:string,
      /**  Site defined in MES.  */  
   newSite:string,
}

export interface CheckUserSiteAccess_output{
      /**  Returns True if the provided user ID has access to the site.  */  
   returnObj:boolean,
}

export interface Erp_Tablesets_MESMenuRow{
      /**  Company, if MESMenu row is generated data. For system data this is empty.  */  
   Company:string,
      /**  Unique identifier for the record  */  
   MESMenuID:number,
      /**  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  */  
   ParentMESMenuID:number,
      /**  Type of menu. H = Handheld MES / M = MES  */  
   MenuType:string,
      /**  Used to sort the items on the Handheld MES menu. Low to high.  */  
   Seq:number,
      /**  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  */  
   MenuID:string,
      /**  The description that appears on the Handheld MES menu and in the maintenance program.  */  
   MenuDesc:string,
      /**  True if the item should be hidden from the Handheld MES menu.  */  
   Hidden:boolean,
      /**  True if row is system data, false for data generated for specific company  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   MESMaterialHandler:boolean,
   MESSupervisor:boolean,
   MESShipping:boolean,
   MESProduction:boolean,
   MESService:boolean,
   PCIDInbound:boolean,
   PCIDOutbound:boolean,
   PCIDInventory:boolean,
   PCIDManufacturing:boolean,
   PCIDQuality:boolean,
   CurrentEmpAllowed:boolean,
   TranslateMenuDesc:string,
      /**  Indicates if the row is disabled  */  
   DisableRow:boolean,
   EnablePackageControl:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MESMenuSecurityRow{
      /**  Company, if MESMenu row is generated data. For system data this is empty.  */  
   Company:string,
      /**  The unique idenfiier of the MESMenu record this record pertains to  */  
   MESMenuID:number,
      /**  The group the role belongs to. M = Traditional MES/ P = Package Control  */  
   SecurityGroup:string,
      /**  The role from a set of predefined roles that is required to access the item  */  
   Role:string,
      /**  True if row is system data, false for data generated for specific company  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MESMenuTableset{
   MESMenu:Erp_Tablesets_MESMenuRow[],
   MESMenuSecurity:Erp_Tablesets_MESMenuSecurityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
      @param menuTypes
   */  
export interface GetMenuData_input{
      /**  Empty if called from maintenance UI, currently selected employee ID if called from menus  */  
   empID:string,
      /**  MenuType to retrieve. Blank for all. Accepts multiple ~ delimited values.  */  
   menuTypes:string,
}

export interface GetMenuData_output{
   returnObj:Erp_Tablesets_MESMenuTableset[],
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
      @param mesMenuTS
      @param fullMenuList
      @param recreateFromSeedData
   */  
export interface ImportMESMenuData_input{
   mesMenuTS:Erp_Tablesets_MESMenuTableset[],
      /**  Indicates the type of process to run: if True, then a full dataset process. This includes deleting exsiting seed data. If False, then an incremental partial dataset process. There is no elements deletion in this case.  */  
   fullMenuList:boolean,
      /**  Indicates if a recreation of the Menus based on the current seed data is required before the data processing. When True, then dataset is optional.  */  
   recreateFromSeedData:boolean,
}

export interface ImportMESMenuData_output{
}

   /** Required : 
      @param overwriteExisting
   */  
export interface InitializeMESMenu_input{
      /**  Set to true to overwrite existing MESMenu data.  */  
   overwriteExisting:boolean,
}

export interface InitializeMESMenu_output{
}

   /** Required : 
      @param EmployeeID
   */  
export interface SetEmployeeID_input{
   EmployeeID:string,
}

export interface SetEmployeeID_output{
parameters : {
      /**  output parameters  */  
   DcdUserID:string,
   LoginRequired:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateMenuData_input{
   ds:Erp_Tablesets_MESMenuTableset[],
}

export interface UpdateMenuData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MESMenuTableset[],
}
}

