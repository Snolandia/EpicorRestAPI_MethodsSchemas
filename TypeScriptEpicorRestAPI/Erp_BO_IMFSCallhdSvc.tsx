import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMFSCallhdSvc
// Description: Business Object to handle: Count, Get, Ack, and GetAll of FSCallhd
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata", {
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
   Summary: Invoke method AckFSCallhd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckFSCallhd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/AckFSCallhd", {
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
   Summary: Invoke method CountFSCallhd
   Description: Returns the count of existing IntQueOut records along with the count of updated FSCallhds in the database that IntQueOut records have not yet been created for
   OperationID: CountFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountFSCallhd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/CountFSCallhd", {
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
   Summary: Invoke method GetAllFSCallhd
   Description: Generates IntQueOut and IMFSCallhd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllFSCallhd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/GetAllFSCallhd", {
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
   Summary: Invoke method GetFSCallhd
   Description: Generates IntQueOut and IMFSCallhd rows since the last time this was called and then returns these along with any existing
   OperationID: GetFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFSCallhd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/GetFSCallhd", {
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
      @param ts
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckFSCallhd_input{
   ts:Erp_Tablesets_IMFSCallhdTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckFSCallhd_output{
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
export interface CountFSCallhd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountFSCallhd_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMFSCallDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Serial number of the part being repaired.  */  
   SerialNumber:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Unique code for the Warranty  */  
   WarrantyCode:string,
      /**  Contract Number if this item is under a contract  */  
   ContractNum:number,
      /**  This is the contract line the relates to the item on the service call.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   CallComment:string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Problem reason code from the reason master table. type problem.  */  
   ProbReasonCode:string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  total Labor Amount.  */  
   TotLabor:number,
      /**  total Labor Amount. In customers currency  */  
   DocTotLabor:number,
      /**  total Billable Labor Amount.  */  
   TotBillLabor:number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   DocTotBillLabor:number,
      /**  total Material Amount.  */  
   TotMaterial:number,
      /**  total Material Amount. In Customers currency  */  
   DocTotMaterial:number,
      /**  total Billable Material Amount.  */  
   TotBillMaterial:number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   DocTotBillMaterial:number,
      /**  total Misc. Amount.  */  
   TotMisc:number,
      /**  total Misc. Amount. In customers currency.  */  
   DocTotMisc:number,
      /**  total Billable Misc. Amount.  */  
   TotBillableMisc:number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   DocTotBillableMisc:number,
      /**  total Material Cost.  */  
   TotMaterialCost:number,
      /**  total Misc. Cost.  */  
   TotMiscCost:number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   ProjectID:string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total Subcontract Amount.  */  
   TotSubCont:number,
      /**  total Subcontract Amount. In customers currency  */  
   DocTotSubCont:number,
      /**  total Billable Subcontract Amount.  */  
   TotBillSubCont:number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   DocTotBillSubCont:number,
      /**  total Estimated Labor Amount.  */  
   TotEstLabor:number,
      /**  total estimated Labor Amount. In customers currency  */  
   DocTotEstLabor:number,
      /**  total Estimated Material Amount.  */  
   TotEstMaterial:number,
      /**  total Estimated Material Amount. In Customers currency  */  
   DocTotEstMaterial:number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   TotEstMisc:number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   DocTotEstMisc:number,
      /**  Total estimated Subcontract Amount.  */  
   TotEstSubCont:number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   DocTotEstSubCont:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotSubCont:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   VendorNum:number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   PurPoint:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  POLine  */  
   POLine:string,
      /**  IssueTopicID1  */  
   IssueTopicID1:string,
      /**  IssueTopicID2  */  
   IssueTopicID2:string,
      /**  IssueTopicID3  */  
   IssueTopicID3:string,
      /**  IssueTopicID4  */  
   IssueTopicID4:string,
      /**  IssueTopicID5  */  
   IssueTopicID5:string,
      /**  IssueTopicID6  */  
   IssueTopicID6:string,
      /**  IssueTopicID7  */  
   IssueTopicID7:string,
      /**  IssueTopicID8  */  
   IssueTopicID8:string,
      /**  IssueTopicID9  */  
   IssueTopicID9:string,
      /**  IssueTopicID10  */  
   IssueTopicID10:string,
      /**  IssueTopics  */  
   IssueTopics:string,
      /**  ResTopicID1  */  
   ResTopicID1:string,
      /**  ResTopicID2  */  
   ResTopicID2:string,
      /**  ResTopicID3  */  
   ResTopicID3:string,
      /**  ResTopicID4  */  
   ResTopicID4:string,
      /**  ResTopicID5  */  
   ResTopicID5:string,
      /**  ResTopicID6  */  
   ResTopicID6:string,
      /**  ResTopicID7  */  
   ResTopicID7:string,
      /**  ResTopicID8  */  
   ResTopicID8:string,
      /**  ResTopicID9  */  
   ResTopicID9:string,
      /**  ResTopicID10  */  
   ResTopicID10:string,
      /**  ResTopics  */  
   ResTopics:string,
      /**  PartDescription  */  
   PartDescription:string,
      /**  CommentText  */  
   CommentText:string,
      /**  Indicates the invoice processing has been done for this call line.  */  
   Invoiced:boolean,
      /**  Indicates that the call line can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSCallhdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  defaults to TODAY  */  
   EntryDate:string,
      /**  Time in second past midnight  */  
   EntryTime:number,
      /**  The date that the service is requested for.  */  
   RequestDate:string,
      /**  Time in second past midnight  */  
   RequestTime:number,
      /**  The date that the service is scheduled for.  */  
   SchedDate:string,
      /**  Time in second past midnight  */  
   SchedTime:number,
      /**  The date that the service was performed on.  */  
   ActualDate:string,
      /**  Time in second past midnight  */  
   ActualTime:number,
      /**  Contains comments about the overall Call. These will be printed on the Service Call.  */  
   CallComment:string,
      /**  Contains comments about the overall Call. These will be printed on the Service Call invoice.  */  
   InvoiceComment:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Indicate that the call is open.  */  
   OpenCall:boolean,
      /**  Indicates that the call is closed and can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Indicated the invoice processing has been done for this call.  */  
   Invoiced:boolean,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   VoidCall:boolean,
      /**  Can have 3 values High, normal and, Low  */  
   CallPriority:string,
      /**   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  A unique code that identifies the type of service call  */  
   CallCode:string,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  */  
   LaborComplete:boolean,
      /**  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  */  
   MaterialComplete:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The estimated duration of the service call in days.  */  
   Duration:number,
      /**  The Clientele call number that is related to this call.  */  
   CLCallNum:string,
      /**  The help desk case that created this service call.  */  
   HDCaseNum:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping country number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PONum  */  
   PONum:string,
      /**  Determines if the service call has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   CustID:string,
   CallDescription:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
   ShipToName:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMFSCallhdTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMFSCallDt:Erp_Tablesets_IMFSCallDtRow[],
   IMFSCallhd:Erp_Tablesets_IMFSCallhdRow[],
   IMFsTech:Erp_Tablesets_IMFsTechRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMFsTechRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The call number that the technician is assigned to.  */  
   CallNum:number,
      /**  Part of the unique for this table.  */  
   SeqNum:number,
      /**  Employee ID.  */  
   EmpID:string,
      /**  the name of the employee assigned to the service call.  */  
   Name:string,
      /**  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  */  
   OpenCall:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   CnvEmpID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
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
export interface GetAllFSCallhd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllFSCallhd_output{
   returnObj:Erp_Tablesets_IMFSCallhdTableset[],
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
export interface GetFSCallhd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetFSCallhd_output{
   returnObj:Erp_Tablesets_IMFSCallhdTableset[],
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

