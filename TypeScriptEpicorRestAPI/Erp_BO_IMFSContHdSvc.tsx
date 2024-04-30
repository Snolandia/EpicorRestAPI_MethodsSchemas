import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMFSContHdSvc
// Description: Bi-Directional integration point for FSContHd, FSContDt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", {
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
   Summary: Invoke method AckFSContHd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckFSContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AckFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckFSContHd(requestBody:AckFSContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AckFSContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/AckFSContHd", {
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
         resolve(data as AckFSContHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CountFSContHd
   Description: Returns the count of existing IntQueOut records along with the count of updated FSContHd in the database that IntQueOut records have not yet been created for
   OperationID: CountFSContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CountFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountFSContHd(requestBody:CountFSContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CountFSContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/CountFSContHd", {
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
         resolve(data as CountFSContHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllFSContHd
   Description: Generates IntQueOut and IMFSContHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllFSContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllFSContHd(requestBody:GetAllFSContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllFSContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/GetAllFSContHd", {
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
         resolve(data as GetAllFSContHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFSContHd
   Description: Generates IntQueOut and IMFSContHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetFSContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFSContHd(requestBody:GetFSContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFSContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/GetFSContHd", {
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
         resolve(data as GetFSContHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteFSContHd
   Description: Delete contract and contract related tables
   OperationID: DeleteFSContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFSContHd(requestBody:DeleteFSContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteFSContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/DeleteFSContHd", {
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
         resolve(data as DeleteFSContHd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddFsContHd
   Description: Add customer and customer related tables
   OperationID: AddFsContHd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddFsContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddFsContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddFsContHd(requestBody:AddFsContHd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddFsContHd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/AddFsContHd", {
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
         resolve(data as AddFsContHd_output)
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
export interface AckFSContHd_input{
   ts:Erp_Tablesets_IMFSContHdTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckFSContHd_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param IMFSContHdTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddFsContHd_input{
   IMFSContHdTableset:Erp_Tablesets_IMFSContHdTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddFsContHd_output{
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
export interface CountFSContHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountFSContHd_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

   /** Required : 
      @param IMFSContHdTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface DeleteFSContHd_input{
   IMFSContHdTableset:Erp_Tablesets_IMFSContHdTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface DeleteFSContHd_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

export interface Erp_Tablesets_IMFSContDtRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  */  
   ContractComment:string,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSContHdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Same as OrderDate when SLSORD.  TODAY when CNTENT  */  
   EntryDate:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the overall Contract. These will be printed on the Service Contract.  */  
   ContractComment:string,
      /**  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  */  
   ActiveDate:string,
      /**   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  */  
   ExpireDate:string,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Whether the duration is for Days, Months, years.  */  
   Modifier:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the service contract using is valid for renewal.  */  
   Renewable:boolean,
      /**  Determines if the service contract has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  */  
   FSAServiceAgreementNum:number,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSContHdTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMFSContDt:Erp_Tablesets_IMFSContDtRow[],
   IMFSContHd:Erp_Tablesets_IMFSContHdRow[],
   IMFSContSN:Erp_Tablesets_IMFSContSNRow[],
   IMFSRenewal:Erp_Tablesets_IMFSRenewalRow[],
   IMFSRenewalDt:Erp_Tablesets_IMFSRenewalDtRow[],
   IMFSRenewalSN:Erp_Tablesets_IMFSRenewalSNRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMFSContSNRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   PartNum:string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   SerialNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Key of related IntQueInOut record  */  
   IntQueID:number,
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSRenewalDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   RenewalLine:number,
      /**  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  */  
   ContractLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  */  
   IUM:string,
      /**  Total Contract Quantity for the line item.  */  
   ContractQty:number,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  */  
   CustNum:number,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  */  
   Inactive:boolean,
      /**  This is the first date the contract line is considered for billing purposes.  */  
   BillStartDate:string,
      /**  This is the last date the contract line is considered for billing.  */  
   BillEndDate:string,
      /**  Indicates this line has been invoiced.  */  
   Invoiced:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Key of related IntQueInOut record  */  
   IntQueID:number,
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSRenewalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Used to establish invoice comments about the overall Renewal.  */  
   RenewalComment:string,
      /**  Date when the renewal begins.  */  
   RenewEffDate:string,
      /**  Date the renewal ends.  */  
   RenewedUntil:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  It is the same as the contract type but applied to renewals  */  
   ContractCode:string,
      /**  The unit of measure of time that the renewal contract lasts.  */  
   Modifier:string,
      /**  Key of related IntQueInOut record  */  
   IntQueID:number,
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSRenewalSNRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Contract Number of the Contract  */  
   ContractNum:number,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  This field along with Company and ContractNum make up the unique key to the table.  */  
   RenewalLine:number,
      /**  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  */  
   PartNum:string,
      /**  Serial number of the Part that is assigned to this Field Service contract line.  */  
   SerialNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Key of related IntQueInOut record  */  
   IntQueID:number,
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
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
export interface GetAllFSContHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllFSContHd_output{
   returnObj:Erp_Tablesets_IMFSContHdTableset[],
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
export interface GetFSContHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetFSContHd_output{
   returnObj:Erp_Tablesets_IMFSContHdTableset[],
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

