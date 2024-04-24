import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobManagerSvc
// Description: JobManager, is an object which works with the Demand and Supply of a specific part number.
Provides dataset of Demand/Supply relationships matrix.
Provides methods for maintaining these relationships
Provides access to the Suggestions for a given part
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", {
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
   Summary: Invoke method FindPart
   Description: Retrieves part number
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/FindPart", {
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
   Summary: Invoke method GetPartFromRowID
   Description: Use SysrowID to find the part
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/GetPartFromRowID", {
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
   Summary: Invoke method CheckPartStatus
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, if any substitutes exist and Message type.
Intended to be called prior to calling the CreateJob method.
   OperationID: CheckPartStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/CheckPartStatus", {
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
   Summary: Invoke method CreateJob
   Description: To create a new Job for production demand.
You pass this method the Reckey of the demand record for which a job will be created.
The job will be created and this demand record will be linked to it.
You must also pass the Job Number you wish to use. This should have been determined
using the standard object to assign job numbers.
IMPORTANT: Your logic should have also called the CheckPartStatus method and provided the appropriate
user interaction before calling this mehtod.
   OperationID: CreateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/CreateJob", {
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
   Summary: Invoke method DeleteJob
   Description: To delete the Job of a specific JMSupply record.
   OperationID: DeleteJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/DeleteJob", {
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
   Summary: Invoke method DeletePartSug
   Description: Deletes Part Suggestion
   OperationID: DeletePartSug
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePartSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePartSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePartSug(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/DeletePartSug", {
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
   Summary: Invoke method GetMatrix
   Description: To retrieve the JobManager dataset for a given part number.
This dataset is a Demand/Supply matrix for the part.
Note: Part numbers may not exist in the Part table. Therefore, this method allows you to pass in
the part description. Depending on where you are calling from, you might use OrderDtl.LineDesc,
JobMtl.Description, etc.
   OperationID: GetMatrix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatrix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatrix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatrix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/GetMatrix", {
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
   Summary: Invoke method GetNextJobNumOrderRelease
   Description: This methods generates the job number based off
of the OrderRel record related to the input PartDtl.
   OperationID: GetNextJobNumOrderRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextJobNumOrderRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextJobNumOrderRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextJobNumOrderRelease(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/GetNextJobNumOrderRelease", {
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
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/GetPartXRefInfo", {
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
   Summary: Invoke method LinkToJob
   Description: To link a production demand (JMDemand record) with an existing job.
This validates the following:
1. The demand record still exists in the database.
2. That it is not already linked to a source of supply (job, warehouse)
3. Target job exists.
4. Target job is not a Field Service Job.
5. System configuration allows changes to engineered Jobs.
6. Job is not Closed.
   OperationID: LinkToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkToJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/LinkToJob", {
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
   Summary: Invoke method PreGetDetails
   Description: This method checks to see if the part is a valid part in the part master.
Configured parts have the option to create part numbers without create a part
record.  If this is the case, then use the OrderDtl.BasePartNum and
OrderDtl.BaseRevisionNum or QuoteDtl.BasePartNum and QuoteDtl.BaseRevisionNum
to get details.  If the basePartNum isn't equal to null then use it to Get Details
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGetDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/PreGetDetails", {
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
   Summary: Invoke method PullFromStock
   Description: To link a demand with to a warehouse that will supply the demand.
   OperationID: PullFromStock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PullFromStock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PullFromStock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PullFromStock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/PullFromStock", {
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
   Summary: Invoke method TransferDemand
   Description: To transfer a demand on one job to another job.
   OperationID: TransferDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransferDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferDemand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/TransferDemand", {
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
   Summary: Invoke method UnlinkDemand
   Description: To unlink a demand from the related Job.
   OperationID: UnlinkDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkDemand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/UnlinkDemand", {
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
   Summary: Invoke method UnlinkSupply
   Description: To unlink a supply from it's related demand.
   OperationID: UnlinkSupply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkSupply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkSupply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkSupply(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/UnlinkSupply", {
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
      @param partNum
   */  
export interface CheckPartStatus_input{
      /**  The part number to validate  */  
   partNum:string,
}

export interface CheckPartStatus_output{
parameters : {
      /**  output parameters  */  
   vMsgText:string,
   vSubAvail:boolean,
   vMsgType:string,
}
}

   /** Required : 
      @param demandReckey
      @param newJobNum
   */  
export interface CreateJob_input{
      /**  The JMDemand.RecKey field value of row for which a new job will be created.  */  
   demandReckey:string,
      /**  Job number to be assigned to the newly created job  */  
   newJobNum:string,
}

export interface CreateJob_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param jmSupply_RecKey
   */  
export interface DeleteJob_input{
      /**  The JMSupply.Reckey field is the physical rowid of the JobPart record.
Therefore it can be used to indicate the job that you wish deleted.  */  
   jmSupply_RecKey:string,
}

export interface DeleteJob_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param partSug_RowID
   */  
export interface DeletePartSug_input{
      /**  Part Suggestions Row id  */  
   partSug_RowID:string,
}

export interface DeletePartSug_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

export interface Erp_Tablesets_JMDemandRow{
      /**  RecKey of the Parent record (JMPartSum)  */  
   ParentRecKey:string,
      /**  Unique Key - Uses RowID of the PartDtl which was the data source  */  
   RecKey:string,
   DueDate:string,
   Quantity:number,
   JobNum:string,
      /**  Formatted String representing Source of Demand. Ex: SO 105-3-1 means Sales Order 105 Line 3 Release 1  */  
   SourceString:string,
   FirmRelease:boolean,
   OrderNum:number,
   Plant:string,
   CustomerName:string,
      /**  N = New, C = Change, " " = No Suggestions. Used for filtering.  */  
   SuggestionFlag:string,
   OrderLine:number,
   OrderRelNum:number,
      /**  Indicates if create Job function is available for this record  */  
   CanCreateJob:boolean,
      /**  Indicates if Pull from Stock function is available for this record  */  
   CanPull:boolean,
      /**  Indicates if this Demand has one or more related DemandSupply records  */  
   Linked:boolean,
      /**  Text description of the SuggestionFlag field for transalation N=new, C=Change, ""=None  */  
   SuggestionFlagDesc:string,
      /**  If this JMDemand record is associated with a PartSug record, this field is true.  */  
   HasSuggestion:boolean,
      /**  Description from PartSug.Description field  */  
   PartSugDesc:string,
      /**  either the rowid from PartDtl or PartSug  */  
   UniqueRecKey:string,
   UOM:string,
   ContractID:string,
   LinkToContract:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JMDemandSupplyRow{
      /**  RecKey of the Parent record (JMDemand)  */  
   ParentRecKey:string,
      /**  Unique Key - RowID of the datasoure record (JobProd, PartDtl, OrderRel, JobMtl,JobAsmbl). Datasource table is identified in SourcTable field.  */  
   RecKey:string,
      /**  The main DB Source table that data in this record was derived from. Note: Reckey contains the RowID of the record from this table.  */  
   SourceTable:string,
      /**  Formatted String representing Source of supply. Ex: Whse MPL  means supplied from Stock Warehouse Mpl  */  
   SourceString:string,
      /**  Required By date of the supply  */  
   ReqDate:string,
   Quantity:number,
   JobComplete:boolean,
   JobReleased:boolean,
   ProdQty:number,
   RelievedQty:number,
   JobNum:string,
   WareHouseCode:string,
      /**  Indicates if Transfer function is appropriate for this record  */  
   Transferable:boolean,
   WarehouseDescription:string,
   CanUnLink:boolean,
      /**  Quantity IUM  */  
   QuantityUOM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JMInventoryRow{
      /**  RecKey of the Parent record (JMPartSum)  */  
   ParentRecKey:string,
      /**  Unique Key - Uses RowID of the PartWhse which was the data source  */  
   RecKey:string,
   Plant:string,
   WarehouseCode:string,
   OnHandQty:number,
   AvailQty:number,
   WarehouseDescription:string,
   DemandQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JMPartSumRow{
      /**  Unique Key - Uses the PartNum as the value.  */  
   RecKey:string,
   PartNum:string,
      /**  Quantity on hand, entire company  */  
   OnHandQty:number,
      /**  Part Quantity Available  - Entire Company  */  
   AvailQty:number,
   PartDescription:string,
      /**  Part UOM  */  
   UOM:string,
      /**  Demand - Entire Company/All warehouses  */  
   DemandQty:number,
   ContractDescription:string,
   ContractID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JMSupplyDemandRow{
      /**  RecKey of the Parent record (JMSupply)  */  
   ParentRecKey:string,
      /**  Unique Key - RowID of the datasoure record (JobProd).  */  
   RecKey:string,
   SourceString:string,
   ShipByDate:string,
   WipQty:number,
   ProdQty:number,
   RelievedQty:number,
   OrderNum:number,
   JobNum:string,
   DemandStatus:string,
      /**  Indicates if transfer function is available for this record.  */  
   Transferable:boolean,
   CanUnLink:boolean,
      /**  Flag that indicates if it is a service job  */  
   IsServiceJob:boolean,
      /**  Engineered or not.  */  
   JobEngineered:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JMSupplyRow{
      /**  RecKey of the Parent record (JMPartSum)  */  
   ParentRecKey:string,
      /**  Unique Key - Uses RowID of the JobHead which was the data source  */  
   RecKey:string,
   ReqDate:string,
   JobNum:string,
   WipQty:number,
   JobReleased:boolean,
   JobComplete:boolean,
   ProdQty:number,
   RelievedQty:number,
   QtyCompleted:number,
      /**  Indicates if demands can be linked to this supply.  */  
   Linkable:boolean,
      /**  Flag to indicate to the UI if the Get Details button should be enabled.  */  
   EnableGetDetails:boolean,
      /**  Flag to indicate to UI if the Delete Job button should be enabled.  */  
   EnableDeleteJob:boolean,
      /**  Engineered or not.  */  
   JobEngineered:boolean,
      /**  Flag to indicate to UI if the Schedule button should be enabled.  */  
   EnableSchedule:boolean,
      /**  Indicates if split job is accessible  */  
   EnableSplitJob:boolean,
      /**  If this JMSupply record is associated with a PartSug record, this field is true.  */  
   HasSuggestion:boolean,
      /**  Description from PartSug.Description  */  
   PartSugDesc:string,
      /**  RecKey of the associated PartSug record  */  
   PartSugRecKey:string,
      /**  Flag that indicates if it is a service job  */  
   IsServiceJob:boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   IgnoreMtlConstraints:boolean,
   JobDueDate:string,
   ContractID:string,
   LinkToContract:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobManagerTableset{
   JMPartSum:Erp_Tablesets_JMPartSumRow[],
   JMDemand:Erp_Tablesets_JMDemandRow[],
   JMDemandSupply:Erp_Tablesets_JMDemandSupplyRow[],
   JMInventory:Erp_Tablesets_JMInventoryRow[],
   PartSug:Erp_Tablesets_PartSugRow[],
   JMSupply:Erp_Tablesets_JMSupplyRow[],
   JMSupplyDemand:Erp_Tablesets_JMSupplyDemandRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartSugRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  */  
   Classifier:string,
      /**  New Requirement.  Used to filter between New and Changes.  */  
   NewFlag:boolean,
      /**  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  */  
   Type:string,
      /**   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  */  
   SubType:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Job Number. Think of this as the Job that the suggestion is for ("target job")  */  
   TargetJobNum:string,
      /**  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  */  
   TargetAssemblySeq:number,
      /**  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  */  
   TargetMtlSeq:number,
      /**  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  */  
   Source:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence  */  
   AssemblySeq:number,
      /**  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  */  
   WarehouseCode:string,
      /**   Due date of the related requirement record.
OrderRel.ReqDate.....  */  
   DueDate:string,
      /**  Suggested due date to change meet the requirement.  */  
   SugDate:string,
      /**  Suggested quantity.  */  
   SugQty:number,
      /**  Unit of Measure that qualifies SugQty.  */  
   SugQtyUOM:string,
      /**  Suggested change to Revision Number.  */  
   SugRevisionNum:string,
      /**   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  */  
   Description:string,
      /**  1st 8 characters of customer name. Used for sorting suggestions  */  
   CustShortName:string,
      /**  Duplicated from the customer.custid. Used for sorting purposes.  */  
   CustID:string,
      /**  Purchase order that suggestion is for.  */  
   PONum:number,
      /**  The line # of  PoDetail record suggestion is for.  */  
   POLine:number,
      /**  Purchase order release number that suggestion if for.  */  
   PORelNum:number,
      /**  The ID of the Planner. Used to filter suggestions.  */  
   PlannerID:string,
      /**  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  */  
   FirmRelease:boolean,
      /**   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  */  
   StockTrans:boolean,
      /**  Site Identifier for this manufacturing suggestion.  */  
   Plant:string,
      /**  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  */  
   SugNum:number,
      /**  This is the unique key for the TFOrdDtl table.  */  
   TFLineNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Date and time when this record was created.  */  
   CreatedOn:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   CustFullName:string,
      /**  An error message description.  Used initially when creating a job.  */  
   ErrorMsg:string,
   JobInProcess:boolean,
   Planner:string,
   SugSource:string,
   UOM:string,
   WarehouseDescription:string,
      /**  Used for selecting record on landing page grid for Kinetic version.  */  
   SelectedPartSug:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumReqDueDate:string,
   JobNumStartDate:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  Part Number  */  
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param ipPartNum
      @param ipAttributeSetID
      @param ipPartDescription
      @param uomCode
      @param contractID
      @param contractDesc
   */  
export interface GetMatrix_input{
      /**  Part number to be retrieved.  */  
   ipPartNum:string,
      /**  Attribute Set to be retrieved.  */  
   ipAttributeSetID:number,
      /**  Description of the Part. Optional, used only if the the given part does not exist in the Part table.  */  
   ipPartDescription:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   contractID:string,
   contractDesc:string,
}

export interface GetMatrix_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param ipPartDtlRowid
   */  
export interface GetNextJobNumOrderRelease_input{
      /**  The rowid of the partdtl record to create job for.  */  
   ipPartDtlRowid:string,
}

export interface GetNextJobNumOrderRelease_output{
parameters : {
      /**  output parameters  */  
   opNextJobNum:string,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
      /**  Row Type  */  
   ipRowType:string,
      /**  SysRowID  */  
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param uomCode
      @param sysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
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

   /** Required : 
      @param demandReckey
      @param targetJobNum
   */  
export interface LinkToJob_input{
      /**  The JMDemand.RecKey field value of row to be linked.  */  
   demandReckey:string,
      /**  Job number that you want to link the demand to.  */  
   targetJobNum:string,
}

export interface LinkToJob_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param targetJobNum
      @param targetAsm
   */  
export interface PreGetDetails_input{
      /**  The part number to validate  */  
   partNum:string,
      /**  The revision number to validate  */  
   revisionNum:string,
      /**  Target Job Number  */  
   targetJobNum:string,
      /**  Sequence of the target Assembly  */  
   targetAsm:number,
}

export interface PreGetDetails_output{
parameters : {
      /**  output parameters  */  
   basePartNum:string,
   baseRevisionNum:string,
}
}

   /** Required : 
      @param demandReckey
      @param linkToWareHouseCode
   */  
export interface PullFromStock_input{
      /**  JMDemand.RecKey of the record to be pulled from stock.  */  
   demandReckey:string,
      /**  Warehouse to be pulled from (allocated against).  */  
   linkToWareHouseCode:string,
}

export interface PullFromStock_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param transferRecKey
      @param targetJobNum
   */  
export interface TransferDemand_input{
      /**  TransferRecKey (either DemandSupply or SupplyDemand.RecKey)  of the record to be transferred.  */  
   transferRecKey:string,
      /**  Job Number that the demand will be transfered to.  */  
   targetJobNum:string,
}

export interface TransferDemand_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param supplyDemandReckey
   */  
export interface UnlinkDemand_input{
      /**  JMttJMSupplyDemand.RecKey of the record to be unlinked.  */  
   supplyDemandReckey:string,
}

export interface UnlinkDemand_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

   /** Required : 
      @param demandSupplyReckey
      @param demandSupplySourceTable
   */  
export interface UnlinkSupply_input{
      /**  JMttJMDemandSupply.RecKey of the record to be unlinked.  */  
   demandSupplyReckey:string,
      /**  ttJMDemandSupply.SourceTable of the record to be unlinked.  */  
   demandSupplySourceTable:string,
}

export interface UnlinkSupply_output{
   returnObj:Erp_Tablesets_JobManagerTableset[],
}

