import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMEmpBasicSvc
// Description: Outbound integration point for EmpBasic
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/$metadata", {
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
   Summary: Invoke method AckEmpBasic
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckEmpBasic
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AckEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckEmpBasic(requestBody:AckEmpBasic_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AckEmpBasic_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/AckEmpBasic", {
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
         resolve(data as AckEmpBasic_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CountEmpBasic
   Description: Returns the count of existing IntQueOut records along with the count of updated employees in the database that IntQueOut records have not yet been created for
   OperationID: CountEmpBasic
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CountEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountEmpBasic(requestBody:CountEmpBasic_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CountEmpBasic_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/CountEmpBasic", {
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
         resolve(data as CountEmpBasic_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllEmpBasic
   Description: Generates IntQueOut and IMEmpBasic rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllEmpBasic
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllEmpBasic(requestBody:GetAllEmpBasic_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllEmpBasic_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/GetAllEmpBasic", {
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
         resolve(data as GetAllEmpBasic_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEmpBasic
   Description: Generates IntQueOut and IMEmpBasic rows since the last time this was called and then returns these along with any existing
   OperationID: GetEmpBasic
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpBasic(requestBody:GetEmpBasic_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEmpBasic_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpBasicSvc/GetEmpBasic", {
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
         resolve(data as GetEmpBasic_output)
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
      @param ts
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckEmpBasic_input{
   ts:Erp_Tablesets_IMEmpBasicTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckEmpBasic_output{
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
export interface CountEmpBasic_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountEmpBasic_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMEmpBasicRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  First name of employee.  */  
   FirstName:string,
      /**  Middle name of employee.  */  
   MiddleInitial:string,
      /**  Last name of employee  */  
   LastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   Name:string,
      /**  First Address Line  */  
   Address:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  City portion of address  */  
   City:string,
      /**  Home State. Can be blank.  */  
   State:string,
      /**  Postal Code or Zip code portion of address  */  
   ZIP:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Home phone number  */  
   Phone:string,
      /**  Labor rate that is used for Job Costing.  */  
   LaborRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  This person usually goes out on service calls  */  
   ServTech:boolean,
      /**  Email address of the Employee.  */  
   EMailAddress:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Determines if the employee has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMEmpBasicTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMEmpBasic:Erp_Tablesets_IMEmpBasicRow[],
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
export interface GetAllEmpBasic_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllEmpBasic_output{
   returnObj:Erp_Tablesets_IMEmpBasicTableset[],
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
export interface GetEmpBasic_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetEmpBasic_output{
   returnObj:Erp_Tablesets_IMEmpBasicTableset[],
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

