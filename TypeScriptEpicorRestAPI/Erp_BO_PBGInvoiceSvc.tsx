import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PBGInvoiceSvc
// Description: The PBGInvoice BO.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get PBGInvoices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvoices
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcHeadRow
   */  
export function get_PBGInvoices(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBGInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices", {
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
   Summary: Calls GetByID to retrieve the PBGInvoice item
   Description: Calls GetByID to retrieve the PBGInvoice item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvoice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum(Company:string, ProjectID:string, InvoiceNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBGInvoice for the service
   Description: Calls UpdateExt to update PBGInvoice. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvoice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBGInvoices_Company_ProjectID_InvoiceNum(Company:string, ProjectID:string, InvoiceNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBGInvoice item
   Description: Call UpdateExt to delete PBGInvoice item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvoice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBGInvoices_Company_ProjectID_InvoiceNum(Company:string, ProjectID:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get PBGInvcBdns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcBdns1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcBdnRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcBdns(Company:string, ProjectID:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcBdns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PBGInvcBdn item
   Description: Calls GetByID to retrieve the PBGInvcBdn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcBdn1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RecSeq Desc: RecSeq   Required: True
      @param BdnSetID Desc: BdnSetID   Required: True   Allow empty value : True
      @param BdnCd Desc: BdnCd   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company:string, ProjectID:string, InvoiceNum:string, RecSeq:string, BdnSetID:string, BdnCd:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcBdnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcBdnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PBGInvcDtlFFs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcDtlFFs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlFFRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlFFs(Company:string, ProjectID:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlFFs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PBGInvcDtlFF item
   Description: Calls GetByID to retrieve the PBGInvcDtlFF item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlFF1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcDtlFFRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcDtlFFRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PBGInvcDtlTCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBGInvcDtlTCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlTCRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlTCs(Company:string, ProjectID:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlTCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PBGInvcDtlTC item
   Description: Calls GetByID to retrieve the PBGInvcDtlTC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlTC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcDtlTCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcDtlTCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PBInvoicedAmts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PBInvoicedAmts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBInvoicedAmtRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBInvoicedAmts(Company:string, ProjectID:string, InvoiceNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBInvoicedAmts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PBInvoicedAmt item
   Description: Calls GetByID to retrieve the PBInvoicedAmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBInvoicedAmt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param TranKey Desc: TranKey   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   */  
export function get_PBGInvoices_Company_ProjectID_InvoiceNum_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company:string, ProjectID:string, InvoiceNum:string, RelatedToFile:string, TranKey:string, TaxCatID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBInvoicedAmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvoices(" + Company + "," + ProjectID + "," + InvoiceNum + ")/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBInvoicedAmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PBGInvcBdns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcBdns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcBdnRow
   */  
export function get_PBGInvcBdns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcBdns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBGInvcBdns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns", {
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
   Summary: Calls GetByID to retrieve the PBGInvcBdn item
   Description: Calls GetByID to retrieve the PBGInvcBdn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcBdn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RecSeq Desc: RecSeq   Required: True
      @param BdnSetID Desc: BdnSetID   Required: True   Allow empty value : True
      @param BdnCd Desc: BdnCd   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   */  
export function get_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company:string, ProjectID:string, InvoiceNum:string, RecSeq:string, BdnSetID:string, BdnCd:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcBdnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcBdnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBGInvcBdn for the service
   Description: Calls UpdateExt to update PBGInvcBdn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcBdn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RecSeq Desc: RecSeq   Required: True
      @param BdnSetID Desc: BdnSetID   Required: True   Allow empty value : True
      @param BdnCd Desc: BdnCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcBdnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company:string, ProjectID:string, InvoiceNum:string, RecSeq:string, BdnSetID:string, BdnCd:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBGInvcBdn item
   Description: Call UpdateExt to delete PBGInvcBdn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcBdn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RecSeq Desc: RecSeq   Required: True
      @param BdnSetID Desc: BdnSetID   Required: True   Allow empty value : True
      @param BdnCd Desc: BdnCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBGInvcBdns_Company_ProjectID_InvoiceNum_RecSeq_BdnSetID_BdnCd(Company:string, ProjectID:string, InvoiceNum:string, RecSeq:string, BdnSetID:string, BdnCd:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcBdns(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RecSeq + "," + BdnSetID + "," + BdnCd + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PBGInvcDtlFFs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcDtlFFs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlFFRow
   */  
export function get_PBGInvcDtlFFs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcDtlFFs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBGInvcDtlFFs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs", {
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
   Summary: Calls GetByID to retrieve the PBGInvcDtlFF item
   Description: Calls GetByID to retrieve the PBGInvcDtlFF item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlFF
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   */  
export function get_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcDtlFFRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcDtlFFRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBGInvcDtlFF for the service
   Description: Calls UpdateExt to update PBGInvcDtlFF. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcDtlFF
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlFFRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBGInvcDtlFF item
   Description: Call UpdateExt to delete PBGInvcDtlFF item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcDtlFF
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBGInvcDtlFFs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlFFs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PBGInvcDtlTCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBGInvcDtlTCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcDtlTCRow
   */  
export function get_PBGInvcDtlTCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBGInvcDtlTCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBGInvcDtlTCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs", {
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
   Summary: Calls GetByID to retrieve the PBGInvcDtlTC item
   Description: Calls GetByID to retrieve the PBGInvcDtlTC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBGInvcDtlTC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   */  
export function get_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBGInvcDtlTCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBGInvcDtlTCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBGInvcDtlTC for the service
   Description: Calls UpdateExt to update PBGInvcDtlTC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBGInvcDtlTC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBGInvcDtlTCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBGInvcDtlTC item
   Description: Call UpdateExt to delete PBGInvcDtlTC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBGInvcDtlTC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBGInvcDtlTCs_Company_ProjectID_InvoiceNum_InvoiceLine(Company:string, ProjectID:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBGInvcDtlTCs(" + Company + "," + ProjectID + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PBInvoicedAmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBInvoicedAmts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBInvoicedAmtRow
   */  
export function get_PBInvoicedAmts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBInvoicedAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBInvoicedAmts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts", {
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
   Summary: Calls GetByID to retrieve the PBInvoicedAmt item
   Description: Calls GetByID to retrieve the PBInvoicedAmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBInvoicedAmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param TranKey Desc: TranKey   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   */  
export function get_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company:string, ProjectID:string, InvoiceNum:string, RelatedToFile:string, TranKey:string, TaxCatID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBInvoicedAmtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBInvoicedAmtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBInvoicedAmt for the service
   Description: Calls UpdateExt to update PBInvoicedAmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBInvoicedAmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param TranKey Desc: TranKey   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBInvoicedAmtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company:string, ProjectID:string, InvoiceNum:string, RelatedToFile:string, TranKey:string, TaxCatID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBInvoicedAmt item
   Description: Call UpdateExt to delete PBInvoicedAmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBInvoicedAmt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param TranKey Desc: TranKey   Required: True   Allow empty value : True
      @param TaxCatID Desc: TaxCatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBInvoicedAmts_Company_ProjectID_InvoiceNum_RelatedToFile_TranKey_TaxCatID(Company:string, ProjectID:string, InvoiceNum:string, RelatedToFile:string, TranKey:string, TaxCatID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBInvoicedAmts(" + Company + "," + ProjectID + "," + InvoiceNum + "," + RelatedToFile + "," + TranKey + "," + TaxCatID + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PBPrjInvcPhaseLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBPrjInvcPhaseLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBPrjInvcPhaseListRow
   */  
export function get_PBPrjInvcPhaseLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBPrjInvcPhaseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBPrjInvcPhaseListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBPrjInvcPhaseLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBPrjInvcPhaseLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists", {
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
   Summary: Calls GetByID to retrieve the PBPrjInvcPhaseList item
   Description: Calls GetByID to retrieve the PBPrjInvcPhaseList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBPrjInvcPhaseList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   */  
export function get_PBPrjInvcPhaseLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBPrjInvcPhaseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBPrjInvcPhaseListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBPrjInvcPhaseList for the service
   Description: Calls UpdateExt to update PBPrjInvcPhaseList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBPrjInvcPhaseList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBPrjInvcPhaseListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBPrjInvcPhaseLists_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBPrjInvcPhaseList item
   Description: Call UpdateExt to delete PBPrjInvcPhaseList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBPrjInvcPhaseList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBPrjInvcPhaseLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBPrjInvcPhaseLists(" + SysRowID + ")", {
          method: 'delete',
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
   Summary: Calls GetRows for the service
   Description: Get PBProjectsLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PBProjectsLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBProjectsListRow
   */  
export function get_PBProjectsLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBProjectsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBProjectsListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PBProjectsLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PBProjectsLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists", {
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
   Summary: Calls GetByID to retrieve the PBProjectsList item
   Description: Calls GetByID to retrieve the PBProjectsList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PBProjectsList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   */  
export function get_PBProjectsLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PBProjectsListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PBProjectsListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PBProjectsList for the service
   Description: Calls UpdateExt to update PBProjectsList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PBProjectsList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PBProjectsListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PBProjectsLists_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PBProjectsList item
   Description: Call UpdateExt to delete PBProjectsList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PBProjectsList
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PBProjectsLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/PBProjectsLists(" + SysRowID + ")", {
          method: 'delete',
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PBGInvcHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadListRow)
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
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePBGInvcHead:string, whereClausePBGInvcBdn:string, whereClausePBGInvcDtlFF:string, whereClausePBGInvcDtlTC:string, whereClausePBInvoicedAmt:string, whereClausePBPrjInvcPhaseList:string, whereClausePBProjectsList:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePBGInvcHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBGInvcHead=" + whereClausePBGInvcHead
   }
   if(typeof whereClausePBGInvcBdn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBGInvcBdn=" + whereClausePBGInvcBdn
   }
   if(typeof whereClausePBGInvcDtlFF!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBGInvcDtlFF=" + whereClausePBGInvcDtlFF
   }
   if(typeof whereClausePBGInvcDtlTC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBGInvcDtlTC=" + whereClausePBGInvcDtlTC
   }
   if(typeof whereClausePBInvoicedAmt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBInvoicedAmt=" + whereClausePBInvoicedAmt
   }
   if(typeof whereClausePBPrjInvcPhaseList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBPrjInvcPhaseList=" + whereClausePBPrjInvcPhaseList
   }
   if(typeof whereClausePBProjectsList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePBProjectsList=" + whereClausePBProjectsList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(projectID:string, invoiceNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof projectID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "projectID=" + projectID
   }
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetByID" + params, {
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
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetCodeDescList", {
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
   Summary: Invoke method ApproveInvoice
   Description: ApproveInvoice.
   OperationID: ApproveInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApproveInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/ApproveInvoice", {
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
   Summary: Invoke method GetDataByProjectID
   Description: Custom GetRows method to retrieve data by ProjectID and ConInvMeth.
   OperationID: GetDataByProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataByProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataByProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataByProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetDataByProjectID", {
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
   Summary: Invoke method GetDataByTempInvoiceNum
   Description: Get temp invoice num to call GetByID procedure.
   OperationID: GetDataByTempInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataByTempInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataByTempInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataByTempInvoiceNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetDataByTempInvoiceNum", {
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
   Summary: Invoke method GetNewPBGInvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBGInvcHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetNewPBGInvcHead", {
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
   Summary: Invoke method GetNewPBGInvcBdn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcBdn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcBdn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcBdn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBGInvcBdn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetNewPBGInvcBdn", {
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
   Summary: Invoke method GetNewPBGInvcDtlFF
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcDtlFF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcDtlFF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcDtlFF_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBGInvcDtlFF(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetNewPBGInvcDtlFF", {
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
   Summary: Invoke method GetNewPBGInvcDtlTC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBGInvcDtlTC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBGInvcDtlTC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBGInvcDtlTC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBGInvcDtlTC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetNewPBGInvcDtlTC", {
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
   Summary: Invoke method GetNewPBInvoicedAmt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPBInvoicedAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPBInvoicedAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPBInvoicedAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPBInvoicedAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetNewPBInvoicedAmt", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PBGInvoiceSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcBdnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBGInvcBdnRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlFFRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBGInvcDtlFFRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcDtlTCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBGInvcDtlTCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBGInvcHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBGInvcHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBGInvcHeadRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBInvoicedAmtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBInvoicedAmtRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBPrjInvcPhaseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBPrjInvcPhaseListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PBProjectsListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PBProjectsListRow[],
}

export interface Erp_Tablesets_PBGInvcBdnRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Project ID.  */  
   "ProjectID":string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   "InvoiceNum":number,
      /**  Burden Set Id  */  
   "BdnSetID":string,
      /**  Burden Code  */  
   "BdnCd":string,
      /**  Burden Percentage  */  
   "BdnPrc":number,
      /**  Burden Labor Amount  */  
   "BdnLbrAmt":number,
      /**  Burden Labor Contract Amount  */  
   "BdnConLbrAmt":number,
      /**  Burden subcontract amount  */  
   "BdnSubAmt":number,
      /**  Burden Material Amount  */  
   "BdnMtlAmt":number,
      /**  Burden Other Direct Cost Amount  */  
   "BdnMiscAmt":number,
      /**   Sequence,
zero for original Invoice when InvoiceNum = 0 , 
next for the recalculations. 
-1 = true up process for whole project  */  
   "RecSeq":number,
      /**  Date of the recalculations  */  
   "RecDate":string,
      /**  Burden Labor Amount in the Project currency  */  
   "DocBdnLbrAmt":number,
      /**  Burden Labor Amount in the Reporting currency  */  
   "Rpt1BdnLbrAmt":number,
      /**  Burden Labor Amount in the Reporting currency  */  
   "Rpt2BdnLbrAmt":number,
      /**  Burden Labor Amount in the Reporting currency  */  
   "Rpt3BdnLbrAmt":number,
      /**  Burden Labor Contract Amount in the Project currency  */  
   "DocBdnConLbrAmt":number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   "Rpt1BdnConLbrAmt":number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   "Rpt2BdnConLbrAmt":number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   "Rpt3BdnConLbrAmt":number,
      /**  Burden subcontract amount in the Project currency  */  
   "DocBdnSubAmt":number,
      /**  Burden subcontract amount in the Reporting currency  */  
   "Rpt1BdnSubAmt":number,
      /**  Burden subcontract amount in the Reporting currency  */  
   "Rpt2BdnSubAmt":number,
      /**  Burden subcontract amount in the Reporting currency  */  
   "Rpt3BdnSubAmt":number,
      /**  Burden Material Amount in the Project currency  */  
   "DocBdnMtlAmt":number,
      /**  Burden Material Amount in the Reporting currency  */  
   "Rpt1BdnMtlAmt":number,
      /**  Burden Material Amount in the Reporting currency  */  
   "Rpt2BdnMtlAmt":number,
      /**  Burden Material Amount in the Reporting currency  */  
   "Rpt3BdnMtlAmt":number,
      /**  Burden Other Direct Cost Amount in the Project currency  */  
   "DocBdnMiscAmt":number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   "Rpt1BdnMiscAmt":number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   "Rpt2BdnMiscAmt":number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   "Rpt3BdnMiscAmt":number,
      /**  Actual total burden amount calculated in True up process, can be set by user.  */  
   "DocActTotalAmt":number,
      /**  Invoiced Burden Amount (total of all elements) in document currency  */  
   "DocInvTotalAmt":number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Base currency  */  
   "ActTotalAmt":number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   "Rpt1ActTotalAmt":number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   "Rpt2ActTotalAmt":number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   "Rpt3ActTotalAmt":number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Project currency  */  
   "InvTotalAmt":number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   "Rpt1InvTotalAmt":number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   "Rpt2InvTotalAmt":number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   "Rpt3InvTotalAmt":number,
      /**  Burden calculated from other burdens according to the rules  */  
   "BdnRuleAmt":number,
      /**  Burden calculated from other burdens according to the rules  in the Project currency  */  
   "DocBdnRuleAmt":number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   "Rpt1BdnRuleAmt":number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   "Rpt2BdnRuleAmt":number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   "Rpt3BdnRuleAmt":number,
      /**  Tax Category ID  */  
   "TaxCatID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "BitFlag":number,
   "BdnCdDescription":string,
   "BdnSetIDDescription":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBGInvcDtlFFRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Project ID.  */  
   "ProjectID":string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   "InvoiceNum":number,
      /**  Sequence  */  
   "InvoiceLine":number,
      /**   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  */  
   "TranType":string,
      /**  File where transaction was from  */  
   "TranFile":string,
      /**  Key to the actual source document  */  
   "TranKey":string,
      /**  Billing Schedule ID  */  
   "BillSchedID":string,
      /**  Manager  */  
   "Manager":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales Order Line  */  
   "OrderLine":number,
      /**  Product Group Code  */  
   "ProdCode":string,
      /**  Retention Percent  */  
   "RetentionPcnt":number,
      /**  Reduce Invoice By Retention  */  
   "ReduceInvByRet":boolean,
      /**  Measured Work ID  */  
   "MeasuredWorkID":string,
      /**  Activity ID  */  
   "DtlSeq":number,
      /**  P=Percentage, H=Hours, C=Cost, L=Linear, M=Monetary  */  
   "ActivityUnit":string,
      /**  Price Per Unit  */  
   "PricePerUnit":number,
      /**  Percentage of Contract  */  
   "ContractPrc":number,
      /**  Parent Work Schedule ID  */  
   "ParentWrkSchID":string,
      /**  Customer Quantity Surveyor  */  
   "CustQtySurveyor":string,
      /**  Approval Amount  */  
   "ApprovalAmt":number,
      /**  Approval Date  */  
   "ApprovalDate":string,
      /**  S = Progress, D = Dispute, A = Approved, P = Posted.  */  
   "ActStatus":string,
      /**  Retention Amount  */  
   "RetentionAmt":number,
      /**  Net Activity Amount  */  
   "NettActivityAmt":number,
      /**  Activity Amount  */  
   "ActivityAmount":number,
      /**  Cost Plus percentage  */  
   "CostPlusPrc":number,
      /**  Quantity Surveyor from the Activity Detail  */  
   "QtySurveyor":string,
      /**  in the Project currency  */  
   "DocApprovalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1ApprovalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2ApprovalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3ApprovalAmt":number,
      /**  in the Project currency  */  
   "DocActivityAmount":number,
      /**  in the Reporting currency  */  
   "Rpt1ActivityAmount":number,
      /**  in the Reporting currency  */  
   "Rpt2ActivityAmount":number,
      /**  in the Reporting currency  */  
   "Rpt3ActivityAmount":number,
      /**  in the Project currency  */  
   "DocRetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1RetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2RetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3RetentionAmt":number,
      /**  in the Project currency  */  
   "DocNettActivityAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1NettActivityAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2NettActivityAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3NettActivityAmt":number,
      /**  Price Per Unit in Document currency  */  
   "DocPricePerUnit":number,
      /**  Price Per Unit in Report Currency 1  */  
   "Rpt1PricePerUnit":number,
      /**  Price Per Unit in Report Currency 2  */  
   "Rpt2PricePerUnit":number,
      /**  Price Per Unit in Report Currency 3  */  
   "Rpt3PricePerUnit":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  */  
   "ARInvoiceLine":number,
      /**  Tax Category ID  */  
   "TaxCatID":string,
      /**  PhaseID  */  
   "PhaseID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "MarkUpAmt":number,
   "DocMarkUpAmt":number,
   "Rpt1MarkUpAmt":number,
   "Rpt2MarkUpAmt":number,
   "Rpt3MarkUpAmt":number,
      /**  Phase Description  */  
   "PhaseDescription":string,
   "BitFlag":number,
   "PBillSchDescription":string,
   "PBSchWrkDescription":string,
   "PBWrkMeasuredDtlDescription":string,
   "PBWrkMeasuredHeadDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBGInvcDtlTCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Project ID.  */  
   "ProjectID":string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   "InvoiceNum":number,
      /**  Sequence  */  
   "InvoiceLine":number,
      /**   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  */  
   "TranType":string,
      /**  File where transaction was from  */  
   "TranFile":string,
      /**  Key to the actual source document  */  
   "TranKey":string,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence of the Job that the labor transaction applies to  */  
   "AssemblySeq":number,
      /**  Sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.  */  
   "OprSeq":number,
      /**  Part Number  */  
   "PartNum":string,
      /**  Material Sequence  */  
   "MatNum":number,
      /**  Employee Number  */  
   "EmployeeNum":string,
      /**  Role Code  */  
   "RoleCd":string,
      /**   List of the values:PROJ = Project, EMPL = Employee,
ROLE = Role, LBR = Labor Details  */  
   "LbrRateFrom":string,
      /**  Charge Rate  */  
   "ChargeRate":number,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  Purchase Order Number  */  
   "PONum":number,
      /**  Purchase Order Line  */  
   "POLine":number,
      /**  Purchase Order Release  */  
   "PORelNum":number,
      /**  Packing Slip Line  */  
   "PackLine":number,
      /**  Subcontract Amount  */  
   "SubExtAmt":number,
      /**  subcontract mark up percent  */  
   "PBSubMarkUp":number,
      /**  Subcontract Cost Markup Amount  */  
   "SubMarkUpAmt":number,
      /**  Total Subcontract Amount  */  
   "SubTotalAmt":number,
      /**  Hours  */  
   "Hours":number,
      /**  Labor Amount  */  
   "LbrExtAmt":number,
      /**  Labor Cost Markup percent  */  
   "PBLbrMarkUp":number,
      /**  Labor Cost Amount  */  
   "LbrMarkUpAmt":number,
      /**  Total Labor Amount  */  
   "LbrTotalAmt":number,
      /**  Material Cost  */  
   "MtlCost":number,
      /**  Material  Amount  */  
   "MtlExtAmt":number,
      /**  Material mark up percent  */  
   "PBMtlMarkUp":number,
      /**  Material Cost Amount  */  
   "MtlMarkUpAmt":number,
      /**  Total Material Amount  */  
   "MtlTotalAmt":number,
      /**  Total Ceiling  */  
   "PBCeilingTotal":number,
      /**  Fee Ceiling  */  
   "PBCeilingFee":number,
      /**  Other Cost Ceiling  */  
   "PBCeilingMisc":number,
      /**  Burden Ceiling  */  
   "PBCeilingBur":number,
      /**  Material Burden Ceiling  */  
   "PBCeilingMtlBur":number,
      /**  Material Ceiling  */  
   "PBCeilingMtl":number,
      /**  Subcontract Ceiling  */  
   "PBCeilingSub":number,
      /**  Labor Ceiling  */  
   "PBCeilingLbr":number,
      /**  Individual Ceilings on Suppliers  */  
   "PBIndCeilingSup":boolean,
      /**  Individual Ceilings on Employee  */  
   "PBIndCeilingEmp":boolean,
      /**  Individual Ceilings on Project Role  */  
   "PBIndCeilingPRole":boolean,
      /**  Project Over Ceiling  */  
   "OverCeilingPrj":number,
      /**  Fee Over Ceiling  */  
   "OverCeilingFee":number,
      /**  Burden Over Ceiling  */  
   "OverCeilingBur":number,
      /**  Other Cost Over Ceiling  */  
   "OverCeilingMisc":number,
      /**  Subcontract Over Ceiling  */  
   "OverCeilingSub":number,
      /**  Material Burden Over Ceiling  */  
   "OverCeilingMtlBur":number,
      /**  Material Over Ceiling  */  
   "OverCeilingMtl":number,
      /**  Labor Over Ceiling  */  
   "OverCeilingLbr":number,
      /**  Retention Amount  */  
   "RetentionAmt":number,
      /**  Retention Percentage  */  
   "RetentionPrcnt":number,
      /**  Contract Labor  */  
   "ContrLbr":boolean,
      /**  Transaction Quantity  */  
   "TranQty":number,
      /**   Following options: PRJ = Project Price List,
CUS = Customer Price List, GEN = General Price List, TRN = Transaction  */  
   "PriceFrom":string,
      /**  Transaction Type  */  
   "PartTranType":string,
      /**  Reduced Line amount  */  
   "CutLineAmt":number,
      /**  Over Ceiling  */  
   "OverCeilingAmt":number,
      /**  Ceiling  */  
   "CeilingAmt":number,
      /**  Ceiling comes From: RoleCd, Employee, Supplier  */  
   "CeilingFrom":string,
      /**  Current Invoice Amount  */  
   "CurrentInvoicedAmt":number,
      /**  ODC Amount  */  
   "MiscExtAmt":number,
      /**  ODC markup percent. If Invoicing Type = CP then Copy of Project.PBMiscMarkUp  */  
   "PBMiscMarkUp":number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100  */  
   "MiscMarkUpAmt":number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt  */  
   "MiscTotalAmt":number,
      /**  Misc Change ID for TM/CP Invoices  */  
   "MiscCode":string,
      /**  Labor Invoiced Amount  */  
   "LbrInvAmt":number,
      /**  Material Invoiced Amount  */  
   "MtlInvAmt":number,
      /**  Subcontract Invoiced Amount  */  
   "SubInvAmt":number,
      /**  Burden Invoiced Amount  */  
   "BdnInvAmt":number,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "APInvoiceNum":string,
      /**  This field along with Company, VendorNum and APInvoiceNum make up the unique key to the APInvDtl table.  */  
   "APInvoiceLine":number,
      /**  Subcontract labor  */  
   "SubLbrAmt":number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts)  */  
   "SubMtlAmt":number,
      /**  in the Project currency  */  
   "DocLbrExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1LbrExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2LbrExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3LbrExtAmt":number,
      /**  in the Project currency  */  
   "DocLbrMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1LbrMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2LbrMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3LbrMarkUpAmt":number,
      /**  in the Project currency  */  
   "DocLbrTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1LbrTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2LbrTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3LbrTotalAmt":number,
      /**  in the Project currency  */  
   "DocMtlExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1MtlExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2MtlExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3MtlExtAmt":number,
      /**  in the Project currency  */  
   "DocMtlMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1MtlMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2MtlMarkUpAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3MtlMarkUpAmt":number,
      /**  in the Project currency  */  
   "DocMtlTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1MtlTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2MtlTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3MtlTotalAmt":number,
      /**  in the Project currency  */  
   "DocSubExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1SubExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2SubExtAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3SubExtAmt":number,
      /**  Subcontract Cost Markup Amount  in the Project currency  */  
   "DocSubMarkUpAmt":number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   "Rpt1SubMarkUpAmt":number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   "Rpt2SubMarkUpAmt":number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   "Rpt3SubMarkUpAmt":number,
      /**  in the Project currency  */  
   "DocSubTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1SubTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2SubTotalAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3SubTotalAmt":number,
      /**  ODC Amount in the Project currency  */  
   "DocMiscExtAmt":number,
      /**  ODC Amount in the Reporting currency  */  
   "Rpt1MiscExtAmt":number,
      /**  ODC Amount in the Reporting currency  */  
   "Rpt2MiscExtAmt":number,
      /**  ODC Amount in the Reporting currency  */  
   "Rpt3MiscExtAmt":number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Project currency  */  
   "DocMiscMarkUpAmt":number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   "Rpt1MiscMarkUpAmt":number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   "Rpt2MiscMarkUpAmt":number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   "Rpt3MiscMarkUpAmt":number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Project currency  */  
   "DocMiscTotalAmt":number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   "Rpt1MiscTotalAmt":number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   "Rpt2MiscTotalAmt":number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   "Rpt3MiscTotalAmt":number,
      /**  in the Project currency  */  
   "DocMtlCost":number,
      /**  in the Reporting currency  */  
   "Rpt1MtlCost":number,
      /**  in the Reporting currency  */  
   "Rpt2MtlCost":number,
      /**  in the Reporting currency  */  
   "Rpt3MtlCost":number,
      /**  Reduced Line amount in the Project currency  */  
   "DocCutLineAmt":number,
      /**  Reduced Line amount in the Reporting currency  */  
   "Rpt1CutLineAmt":number,
      /**  Reduced Line amount in the Reporting currency  */  
   "Rpt2CutLineAmt":number,
      /**  Reduced Line amount in the Reporting currency  */  
   "Rpt3CutLineAmt":number,
      /**  Ceiling in the Project currency  */  
   "DocCeilingAmt":number,
      /**  Ceiling in the Reporting currency  */  
   "Rpt1CeilingAmt":number,
      /**  Ceiling in the Reporting currency  */  
   "Rpt2CeilingAmt":number,
      /**  Ceiling in the Reporting currency  */  
   "Rpt3CeilingAmt":number,
      /**  Over Ceiling in the Project currency  */  
   "DocOverCeilingAmt":number,
      /**  Over Ceiling in the Reporting currency  */  
   "Rpt1OverCeilingAmt":number,
      /**  Over Ceiling in the Reporting currency  */  
   "Rpt2OverCeilingAmt":number,
      /**  Over Ceiling in the Reporting currency  */  
   "Rpt3OverCeilingAmt":number,
      /**  in the Project currency  */  
   "DocCurrentInvoicedAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1CurrentInvoicedAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2CurrentInvoicedAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3CurrentInvoicedAmt":number,
      /**  Labor Invoiced Amount in the Project currency  */  
   "DocLbrInvAmt":number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   "Rpt1LbrInvAmt":number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   "Rpt2LbrInvAmt":number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   "Rpt3LbrInvAmt":number,
      /**  Material Invoiced Amount in the Project currency  */  
   "DocMtlInvAmt":number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   "Rpt1MtlInvAmt":number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   "Rpt2MtlInvAmt":number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   "Rpt3MtlInvAmt":number,
      /**  Subcontract Invoiced Amount in the Project currency  */  
   "DocSubInvAmt":number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   "Rpt1SubInvAmt":number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   "Rpt2SubInvAmt":number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   "Rpt3SubInvAmt":number,
      /**  Burden Invoiced Amount in the Project currency  */  
   "DocBdnInvAmt":number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   "Rpt1BdnInvAmt":number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   "Rpt2BdnInvAmt":number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   "Rpt3BdnInvAmt":number,
      /**  Subcontract labor in the Project currency  */  
   "DocSubLbrAmt":number,
      /**  Subcontract labor in the Reporting currency  */  
   "Rpt1SubLbrAmt":number,
      /**  Subcontract labor in the Reporting currency  */  
   "Rpt2SubLbrAmt":number,
      /**  Subcontract labor in the Reporting currency  */  
   "Rpt3SubLbrAmt":number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Project currency  */  
   "DocSubMtlAmt":number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   "Rpt1SubMtlAmt":number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   "Rpt2SubMtlAmt":number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   "Rpt3SubMtlAmt":number,
      /**  Role Mark Up percentage  */  
   "PBRoleMarkup":number,
      /**  reference to Pack Slip number  */  
   "PackNum":string,
      /**  Charge Rate  */  
   "DocChargeRate":number,
      /**  Charge Rate  */  
   "Rpt1ChargeRate":number,
      /**  Charge Rate  */  
   "Rpt2ChargeRate":number,
      /**  Charge Rate  */  
   "Rpt3ChargeRate":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  */  
   "ARInvoiceLine":number,
      /**  in the Project currency  */  
   "DocRetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1RetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2RetentionAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3RetentionAmt":number,
      /**  Field to be deleted in Invoice Review, means that the related transaction will be skipped in the Recalculation of the Invoice  */  
   "ToDelete":boolean,
      /**  Flag indicated that the amount has been updated in the Invoice Review program  */  
   "UpdatedAmt":boolean,
      /**  copy from LaborDtl.TimeTypCd  */  
   "TimeTypCd":string,
      /**  Reference to the Parent Line from the Ceiling Line  */  
   "ParentInvoiceLine":number,
      /**  Tax Category ID  */  
   "TaxCatID":string,
      /**  Line Comment  */  
   "Comment":string,
      /**  PhaseID  */  
   "PhaseID":string,
      /**  OrderNum  */  
   "OrderNum":number,
      /**  OrderLine  */  
   "OrderLine":number,
      /**  OrderRelNum  */  
   "OrderRelNum":number,
      /**  UOM  */  
   "UOM":string,
      /**  PriceListCode  */  
   "PriceListCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BreakListCode  */  
   "BreakListCode":string,
   "DspCPMarkUpAmt":number,
   "DspCPMarkUpPrc":number,
   "DspCPTotalAmt":number,
   "DspLbrAssemblySeq":number,
   "DspLbrJobNum":string,
   "DspLbrOprSeq":number,
   "DspMtlAssemblySeq":number,
   "DspMtlJobNum":string,
   "DspMtlOprSeq":number,
   "DspSubAssemblySeq":number,
   "DspSubJobNum":string,
   "DspSubOprSeq":number,
      /**  Phase Description  */  
   "PhaseDescription":string,
   "Rpt1TotLineAmt":number,
   "Rpt2TotLineAmt":number,
   "Rpt3TotLineAmt":string,
   "TotLineAmt":number,
   "CurrencyCode":string,
   "DocTotLineAmt":number,
   "BitFlag":number,
   "EmployeeNumName":string,
   "MiscCodeDescription":string,
   "PartNumPartDescription":string,
   "RoleCdRoleDescription":string,
   "TaxCatIDDescription":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBGInvcHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Project ID.  */  
   "ProjectID":string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  */  
   "InvoiceNum":number,
      /**  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  */  
   "TmpInvcNum":number,
      /**   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  */  
   "ConInvMeth":string,
   "DspProjectInvcNum":string,
      /**  Actual Invoice date  */  
   "InvoiceDate":string,
   "DspInvoiceNum":number,
   "DspTempInvcNum":number,
      /**  Progress Billing - Order Number  */  
   "PBOrderNum":number,
      /**  Progress Billing - Order Line  */  
   "PBOrderLine":number,
      /**  A = Approved, P = Posted, empty - review  */  
   "PrcStatus":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBGInvcHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Project ID.  */  
   "ProjectID":string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  */  
   "InvoiceNum":number,
      /**  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  */  
   "TmpInvcNum":number,
      /**   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  */  
   "ConInvMeth":string,
      /**  Contract Reference  */  
   "ConReference":string,
      /**  Date the user entered in Invoice Preparation form  */  
   "TmpInvcDate":string,
      /**  Actual Invoice date  */  
   "InvoiceDate":string,
      /**  Currency Code of the Contract  */  
   "CurrencyCode":string,
      /**  Rate Type Code  */  
   "RateGrpCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   "LockRate":boolean,
      /**  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  */  
   "ExchangeRate":number,
      /**  P = Percentage, F = Fixed Amount  */  
   "PBFeePrjType":string,
      /**  P = Percentage, F = Fixed Amount  */  
   "PBFeeSubType":string,
      /**  P = Percentage, F = Fixed Amount  */  
   "PBFeeMtlType":string,
      /**  P = Percentage, F = Fixed Amount  */  
   "PBFeeLbrType":string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   "PBFeePrjApply":string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   "PBFeeSubApply":string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   "PBFeeMtlApply":string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   "PBFeeLbrApply":string,
      /**  Project Fee Charge  */  
   "PBFeePrjCharge":number,
      /**  Subcontract Fee Charge  */  
   "PBFeeSubCharge":number,
      /**  Material Fee Charge  */  
   "PBFeeMtlCharge":number,
      /**  Labor Fee Charge  */  
   "PBFeeLbrCharge":number,
      /**  Burden Amount  */  
   "BdnAmt":number,
      /**  Other Direct Coat Amount  */  
   "MiscAmt":number,
      /**  Subcontract Amount  */  
   "SubAmt":number,
      /**  Material Amount  */  
   "MtlAmt":number,
      /**  Labor Amount  */  
   "LbrAmt":number,
      /**  Total Fee  */  
   "PBFeeTotal":number,
      /**  Project Fee Amount  */  
   "PBFeePrjAmt":number,
      /**  Subcontract Fee Amount  */  
   "PBFeeSubAmt":number,
      /**  Material Fee Amount  */  
   "PBFeeMtlAmt":number,
      /**  Labor Fee Amount  */  
   "PBFeeLbrAmt":number,
      /**  N = Net Cost, G = Gross Cost  */  
   "PBFeeApplyOn":string,
      /**  Progress Billing - Order Number  */  
   "PBOrderNum":number,
      /**  Progress Billing - Order Line  */  
   "PBOrderLine":number,
      /**  The percentage to be retained, this can be 0.  */  
   "RetentionPrcnt":number,
      /**  Retention Processing with a system list of options: M - Maximum of Contract Value, I - Invoice Value  */  
   "RetentionProc":string,
      /**  Fee Retention Amount  */  
   "PBFeeRetentionAmt":number,
      /**  Fee Nett Amount  */  
   "PBFeeNettAmt":number,
      /**  Summa of elements amounts  */  
   "InvcTotalSumAmt":number,
      /**  Total amount plus Fee  */  
   "InvcAddFeeAmt":number,
      /**  Total reduced by Ceiling  */  
   "InvcCutCeiling":number,
      /**  Total redused by Retention  */  
   "InvcCutRetention":number,
      /**  Final Total Invoice  */  
   "InvcTotal":number,
      /**  A = Approved, P = Posted, empty - review  */  
   "PrcStatus":string,
      /**  Customer Number  */  
   "CustNum":number,
      /**  Parameter of the Invoice Preparation process  */  
   "PeriodEndDate":string,
      /**  Fee Ceiling  */  
   "PBCeilingFee":number,
      /**  Total Ceiling  */  
   "PBCeilingTotal":number,
      /**  Individual Ceilings on Suppliers  */  
   "PBIndCeilingSup":boolean,
      /**  Individual Ceilings on Employee  */  
   "PBIndCeilingEmp":boolean,
      /**  Individual Ceilings on Role  */  
   "PBIndCeilingPRole":boolean,
      /**  OverCeiling Fees (negative)  */  
   "OverCeilingFees":number,
      /**  OverCeilingTotalAmt  */  
   "OverCeilingTotalAmt":number,
      /**  Retention Amount  */  
   "RetentionAmt":number,
      /**  Percentage of Progress Payment, for PP invoice only.  */  
   "PPAllowPcnt":number,
      /**  Date the invoice was approved for posting  */  
   "ApprovedDate":string,
      /**  Approved by user id  */  
   "ApprovedBy":string,
      /**  in the Project currency  */  
   "DocPBFeeLbrCharge":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeLbrCharge":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeLbrCharge":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeLbrCharge":number,
      /**  in the Project currency  */  
   "DocPBFeeLbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeLbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeLbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeLbrAmt":number,
      /**  in the Project currency  */  
   "DocPBFeeMtlCharge":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeMtlCharge":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeMtlCharge":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeMtlCharge":number,
      /**  in the Project currency  */  
   "DocPBFeeMtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeMtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeMtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeMtlAmt":number,
      /**  in the Project currency  */  
   "DocPBFeeSubCharge":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeSubCharge":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeSubCharge":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeSubCharge":number,
      /**  in the Project currency  */  
   "DocPBFeeSubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeSubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeSubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeSubAmt":number,
      /**  in the Project currency  */  
   "DocPBFeePrjCharge":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeePrjCharge":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeePrjCharge":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeePrjCharge":number,
      /**  in the Project currency  */  
   "DocPBFeeTotal":number,
      /**  in the Reporting currency  */  
   "Rpt1PBFeeTotal":number,
      /**  in the Reporting currency  */  
   "Rpt2PBFeeTotal":number,
      /**  in the Reporting currency  */  
   "Rpt3PBFeeTotal":number,
      /**  in the Project currency  */  
   "DocLbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1LbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2LbrAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3LbrAmt":number,
      /**  in the Project currency  */  
   "DocMtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1MtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2MtlAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3MtlAmt":number,
      /**  in the Project currency  */  
   "DocSubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1SubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2SubAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3SubAmt":number,
      /**  in the Project currency  */  
   "DocBdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1BdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2BdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3BdnAmt":number,
      /**  in the Project currency  */  
   "DocMiscAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1MiscAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2MiscAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3MiscAmt":number,
      /**  Fee Ceiling in the Project currency  */  
   "DocPBCeilingFee":number,
      /**  Fee Ceiling in the Reporting currency  */  
   "Rpt1PBCeilingFee":number,
      /**  Fee Ceiling in the Reporting currency  */  
   "Rpt2PBCeilingFee":number,
      /**  Fee Ceiling in the Reporting currency  */  
   "Rpt3PBCeilingFee":number,
      /**  in the Project currency  */  
   "DocPBCeilingTotal":number,
      /**  in the Reporting currency  */  
   "Rpt1PBCeilingTotal":number,
      /**  in the Reporting currency  */  
   "Rpt2PBCeilingTotal":number,
      /**  in the Reporting currency  */  
   "Rpt3PBCeilingTotal":number,
      /**  OverCeiling Fees (negative) in the Project currency  */  
   "DocOverCeilingFees":number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   "Rpt1OverCeilingFees":number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   "Rpt2OverCeilingFees":number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   "Rpt3OverCeilingFees":number,
      /**  Retention Amount in the Project currency  */  
   "DocRetentionAmt":number,
      /**  Retention Amount in the Reporting currency  */  
   "Rpt1RetentionAmt":number,
      /**  Retention Amount in the Reporting currency  */  
   "Rpt2RetentionAmt":number,
      /**  Retention Amount in the Reporting currency  */  
   "Rpt3RetentionAmt":number,
      /**  OverCeilingTotalAmt in the Project currency  */  
   "DocOverCeilingTotalAmt":number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   "Rpt1OverCeilingTotalAmt":number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   "Rpt2OverCeilingTotalAmt":number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   "Rpt3OverCeilingTotalAmt":number,
      /**  Fee Retention Amount in the Project currency  */  
   "DocPBFeeRetentionAmt":number,
      /**  Fee Retention Amount in the Reporting currency  */  
   "Rpt1PBFeeRetentionAmt":number,
      /**  Fee Retention Amount in the Reporting currency  */  
   "Rpt2PBFeeRetentionAmt":number,
      /**  Fee Retention Amount in the Reporting currency  */  
   "Rpt3PBFeeRetentionAmt":number,
      /**  Fee Nett Amount in the Project currency  */  
   "DocPBFeeNettAmt":number,
      /**  Fee Nett Amount in the Reporting currency  */  
   "Rpt1PBFeeNettAmt":number,
      /**  Fee Nett Amount in the Reporting currency  */  
   "Rpt2PBFeeNettAmt":number,
      /**  Fee Nett Amount in the Reporting currency  */  
   "Rpt3PBFeeNettAmt":number,
      /**  Summa of elements amounts  in the Project currency  */  
   "DocInvcTotalSumAmt":number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   "Rpt1InvcTotalSumAmt":number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   "Rpt2InvcTotalSumAmt":number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   "Rpt3InvcTotalSumAmt":number,
      /**  Total amount plus Fee in the Project currency  */  
   "DocInvcAddFeeAmt":number,
      /**  Total amount plus Fee in the Reporting currency  */  
   "Rpt1InvcAddFeeAmt":number,
      /**  Total amount plus Fee in the Reporting currency  */  
   "Rpt2InvcAddFeeAmt":number,
      /**  Total amount plus Fee in the Reporting currency  */  
   "Rpt3InvcAddFeeAmt":number,
      /**  Total reduced by Ceiling in the Project currency  */  
   "DocInvcCutCeiling":number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   "Rpt1InvcCutCeiling":number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   "Rpt2InvcCutCeiling":number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   "Rpt3InvcCutCeiling":number,
      /**  Final Total Invoice in the Project currency  */  
   "DocInvcTotal":number,
      /**  Final Total Invoice in the Reporting currency  */  
   "Rpt1InvcTotal":number,
      /**  Final Total Invoice in the Reporting currency  */  
   "Rpt2InvcTotal":number,
      /**  Final Total Invoice in the Reporting currency  */  
   "Rpt3InvcTotal":number,
      /**  Labor actual amount  */  
   "SumLbrTotalAmt":number,
      /**  Material actual amount  */  
   "SumMtlTotalAmt":number,
      /**  Subcontract actual amount  */  
   "SumSubTotalAmt":number,
      /**  Burden actual amount  */  
   "SumBdnAmt":number,
      /**  Labor actual amount in the Project currency  */  
   "DocSumLbrTotalAmt":number,
      /**  Labor actual amount in the Reporting currency  */  
   "Rpt1SumLbrTotalAmt":number,
      /**  Labor actual amount in the Reporting currency  */  
   "Rpt2SumLbrTotalAmt":number,
      /**  Labor actual amount in the Reporting currency  */  
   "Rpt3SumLbrTotalAmt":number,
      /**  Material actual amount in the Project currency  */  
   "DocSumMtlTotalAmt":number,
      /**  Material actual amount in the Reporting currency  */  
   "Rpt1SumMtlTotalAmt":number,
      /**  Material actual amount in the Reporting currency  */  
   "Rpt2SumMtlTotalAmt":number,
      /**  Material actual amount in the Reporting currency  */  
   "Rpt3SumMtlTotalAmt":number,
      /**  Subcontract actual amount in the Project currency  */  
   "DocSumSubTotalAmt":number,
      /**  Subcontract actual amount in the Reporting currency  */  
   "Rpt1SumSubTotalAmt":number,
      /**  Subcontract actual amount in the Reporting currency  */  
   "Rpt2SumSubTotalAmt":number,
      /**  Subcontract actual amount in the Reporting currency  */  
   "Rpt3SumSubTotalAmt":number,
      /**  in the Project currency  */  
   "DocSumBdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt1SumBdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt2SumBdnAmt":number,
      /**  in the Reporting currency  */  
   "Rpt3SumBdnAmt":number,
      /**  Project Fee Amount in Document Currency  */  
   "DocPBFeePrjAmt":number,
      /**  Project Fee Amount in Report Currency 1  */  
   "Rpt1PBFeePrjAmt":number,
      /**  Project Fee Amount in Report Currency 2  */  
   "Rpt2PBFeePrjAmt":number,
      /**  Project Fee Amount in Report Currency 3  */  
   "Rpt3PBFeePrjAmt":number,
      /**   Other Direct Cost Fee Type
List of options: P = Percentage, F = Fixed Amount  */  
   "PBFeeMiscType":string,
      /**   Other Direct Cost Fee Apply Type
List of options: F = First Invoice Only, A = All Invoices.  */  
   "PBFeeMiscApply":string,
      /**  Other Direct Cost Fee value being applied  */  
   "PBFeeMiscCharge":number,
      /**  Calculated ODC Fee amount  */  
   "PBFeeMiscAmt":number,
      /**  Other Direct Cost Fee value being applied in the Project currency  */  
   "DocPBFeeMiscCharge":number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   "Rpt1PBFeeMiscCharge":number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   "Rpt2PBFeeMiscCharge":number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   "Rpt3PBFeeMiscCharge":number,
      /**  Calculated ODC Fee amount in the Project currency  */  
   "DocPBFeeMiscAmt":number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   "Rpt1PBFeeMiscAmt":number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   "Rpt2PBFeeMiscAmt":number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   "Rpt3PBFeeMiscAmt":number,
      /**  Retention percentage. How this is used is dependent on RetentionProc field.  */  
   "PBRetentionPcnt":number,
      /**  Flag indicated that one of its lines has been updated or deleted in the Invoice Review program  */  
   "Updated":boolean,
      /**  Indicates if invoice should be auto printed  */  
   "AutoPrint":boolean,
      /**  Fee Invoice Text  */  
   "PBFeeInvoiceText":string,
      /**  Comment  */  
   "Comment":string,
      /**  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  */  
   "PPAllOrderLines":boolean,
      /**  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  */  
   "PPAllPrjJobs":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag indicates if AR invoices are allowed to be generated even if the element is over the predefined ceiling (limit), also indicates if the invoice amount should stay limited or not when ceiling exists. It is copied from the current value of Project flag  */  
   "ConOverCeiling":boolean,
   "AutoPrintReady":boolean,
      /**  Base Currency ID  */  
   "BaseCurrencyID":string,
   "DspInvoiceNum":number,
   "DspTempInvcNum":number,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrName":string,
   "CustNumName":string,
   "CustNumCustID":string,
   "ProjectIDConReference":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBInvoicedAmtRow{
      /**  Company  */  
   "Company":string,
      /**  Project ID  */  
   "ProjectID":string,
      /**  Related To File  */  
   "RelatedToFile":string,
      /**  Transaction Key  */  
   "TranKey":string,
      /**  Amount strored by Invoice Preparation before Posting ,used to appropriate compare with Ceiling  */  
   "DocPrepAmt":number,
      /**  Preparation over ceiling in Base curency  */  
   "PrepOverCeiling":number,
      /**  Preparation over ceiling in Document curency  */  
   "DocPrepOverCeiling":number,
      /**  Generated Over ceiling in Base currency  */  
   "GenOverCeiling":number,
      /**  Generated Over ceiling in Document currency  */  
   "DocGenOverCeiling":number,
      /**  Posted Over Ceiling in Base currency  */  
   "PostOverCeiling":number,
      /**  Posted Over Ceiling in Document currency  */  
   "DocPostOverCeiling":number,
      /**  Ceiling Generated Consumed in Base currency  */  
   "GenAmt":number,
      /**  Ceiling Generated Consumed in Document currency  */  
   "DocGenAmt":number,
      /**  Ceiling Posted Consumed in Base currency  */  
   "PostAmt":number,
      /**  Ceiling Posted Consumed in Document currency  */  
   "DocPostAmt":number,
      /**  Ceiling Preparation Consumed in Document currency  */  
   "PrepAmt":number,
      /**  Ceiling Limit in Base currency  */  
   "CeilingLimit":number,
      /**  Ceiling Limit in Project Currency  */  
   "DocCeilingLimit":number,
      /**  Invoice Number. It's zero for preparation and total values for whole project  */  
   "InvoiceNum":number,
      /**  Tax Category ID  */  
   "TaxCatID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBPrjInvcPhaseListRow{
   "Company":string,
   "ProjectID":string,
   "InvoiceNum":number,
   "PhaseID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PBProjectsListRow{
   "Company":string,
   "ProjectID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipProjectID
      @param askWarning
      @param ds
   */  
export interface ApproveInvoice_input{
      /**  The ProjectID.  */  
   ipProjectID:string,
   askWarning:boolean,
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}

export interface ApproveInvoice_output{
parameters : {
      /**  output parameters  */  
   warnMessage:string,
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param projectID
      @param invoiceNum
   */  
export interface DeleteByID_input{
   projectID:string,
   invoiceNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PBGInvcBdnRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Project ID.  */  
   ProjectID:string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   InvoiceNum:number,
      /**  Burden Set Id  */  
   BdnSetID:string,
      /**  Burden Code  */  
   BdnCd:string,
      /**  Burden Percentage  */  
   BdnPrc:number,
      /**  Burden Labor Amount  */  
   BdnLbrAmt:number,
      /**  Burden Labor Contract Amount  */  
   BdnConLbrAmt:number,
      /**  Burden subcontract amount  */  
   BdnSubAmt:number,
      /**  Burden Material Amount  */  
   BdnMtlAmt:number,
      /**  Burden Other Direct Cost Amount  */  
   BdnMiscAmt:number,
      /**   Sequence,
zero for original Invoice when InvoiceNum = 0 , 
next for the recalculations. 
-1 = true up process for whole project  */  
   RecSeq:number,
      /**  Date of the recalculations  */  
   RecDate:string,
      /**  Burden Labor Amount in the Project currency  */  
   DocBdnLbrAmt:number,
      /**  Burden Labor Amount in the Reporting currency  */  
   Rpt1BdnLbrAmt:number,
      /**  Burden Labor Amount in the Reporting currency  */  
   Rpt2BdnLbrAmt:number,
      /**  Burden Labor Amount in the Reporting currency  */  
   Rpt3BdnLbrAmt:number,
      /**  Burden Labor Contract Amount in the Project currency  */  
   DocBdnConLbrAmt:number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   Rpt1BdnConLbrAmt:number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   Rpt2BdnConLbrAmt:number,
      /**  Burden Labor Contract Amount in the Reporting currency  */  
   Rpt3BdnConLbrAmt:number,
      /**  Burden subcontract amount in the Project currency  */  
   DocBdnSubAmt:number,
      /**  Burden subcontract amount in the Reporting currency  */  
   Rpt1BdnSubAmt:number,
      /**  Burden subcontract amount in the Reporting currency  */  
   Rpt2BdnSubAmt:number,
      /**  Burden subcontract amount in the Reporting currency  */  
   Rpt3BdnSubAmt:number,
      /**  Burden Material Amount in the Project currency  */  
   DocBdnMtlAmt:number,
      /**  Burden Material Amount in the Reporting currency  */  
   Rpt1BdnMtlAmt:number,
      /**  Burden Material Amount in the Reporting currency  */  
   Rpt2BdnMtlAmt:number,
      /**  Burden Material Amount in the Reporting currency  */  
   Rpt3BdnMtlAmt:number,
      /**  Burden Other Direct Cost Amount in the Project currency  */  
   DocBdnMiscAmt:number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   Rpt1BdnMiscAmt:number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   Rpt2BdnMiscAmt:number,
      /**  Burden Other Direct Cost Amount in the Reporting currency  */  
   Rpt3BdnMiscAmt:number,
      /**  Actual total burden amount calculated in True up process, can be set by user.  */  
   DocActTotalAmt:number,
      /**  Invoiced Burden Amount (total of all elements) in document currency  */  
   DocInvTotalAmt:number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Base currency  */  
   ActTotalAmt:number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   Rpt1ActTotalAmt:number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   Rpt2ActTotalAmt:number,
      /**  Actual total burden amount calculated in True up process, can be set by user. in the Reporting currency  */  
   Rpt3ActTotalAmt:number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Project currency  */  
   InvTotalAmt:number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   Rpt1InvTotalAmt:number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   Rpt2InvTotalAmt:number,
      /**  Invoiced Burden Amount (total of all elements) in document currency in the Reporting currency  */  
   Rpt3InvTotalAmt:number,
      /**  Burden calculated from other burdens according to the rules  */  
   BdnRuleAmt:number,
      /**  Burden calculated from other burdens according to the rules  in the Project currency  */  
   DocBdnRuleAmt:number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   Rpt1BdnRuleAmt:number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   Rpt2BdnRuleAmt:number,
      /**  Burden calculated from other burdens according to the rules  in the Reporting currency  */  
   Rpt3BdnRuleAmt:number,
      /**  Tax Category ID  */  
   TaxCatID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   BitFlag:number,
   BdnCdDescription:string,
   BdnSetIDDescription:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBGInvcDtlFFRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Project ID.  */  
   ProjectID:string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   InvoiceNum:number,
      /**  Sequence  */  
   InvoiceLine:number,
      /**   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  */  
   TranType:string,
      /**  File where transaction was from  */  
   TranFile:string,
      /**  Key to the actual source document  */  
   TranKey:string,
      /**  Billing Schedule ID  */  
   BillSchedID:string,
      /**  Manager  */  
   Manager:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales Order Line  */  
   OrderLine:number,
      /**  Product Group Code  */  
   ProdCode:string,
      /**  Retention Percent  */  
   RetentionPcnt:number,
      /**  Reduce Invoice By Retention  */  
   ReduceInvByRet:boolean,
      /**  Measured Work ID  */  
   MeasuredWorkID:string,
      /**  Activity ID  */  
   DtlSeq:number,
      /**  P=Percentage, H=Hours, C=Cost, L=Linear, M=Monetary  */  
   ActivityUnit:string,
      /**  Price Per Unit  */  
   PricePerUnit:number,
      /**  Percentage of Contract  */  
   ContractPrc:number,
      /**  Parent Work Schedule ID  */  
   ParentWrkSchID:string,
      /**  Customer Quantity Surveyor  */  
   CustQtySurveyor:string,
      /**  Approval Amount  */  
   ApprovalAmt:number,
      /**  Approval Date  */  
   ApprovalDate:string,
      /**  S = Progress, D = Dispute, A = Approved, P = Posted.  */  
   ActStatus:string,
      /**  Retention Amount  */  
   RetentionAmt:number,
      /**  Net Activity Amount  */  
   NettActivityAmt:number,
      /**  Activity Amount  */  
   ActivityAmount:number,
      /**  Cost Plus percentage  */  
   CostPlusPrc:number,
      /**  Quantity Surveyor from the Activity Detail  */  
   QtySurveyor:string,
      /**  in the Project currency  */  
   DocApprovalAmt:number,
      /**  in the Reporting currency  */  
   Rpt1ApprovalAmt:number,
      /**  in the Reporting currency  */  
   Rpt2ApprovalAmt:number,
      /**  in the Reporting currency  */  
   Rpt3ApprovalAmt:number,
      /**  in the Project currency  */  
   DocActivityAmount:number,
      /**  in the Reporting currency  */  
   Rpt1ActivityAmount:number,
      /**  in the Reporting currency  */  
   Rpt2ActivityAmount:number,
      /**  in the Reporting currency  */  
   Rpt3ActivityAmount:number,
      /**  in the Project currency  */  
   DocRetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt1RetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt2RetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt3RetentionAmt:number,
      /**  in the Project currency  */  
   DocNettActivityAmt:number,
      /**  in the Reporting currency  */  
   Rpt1NettActivityAmt:number,
      /**  in the Reporting currency  */  
   Rpt2NettActivityAmt:number,
      /**  in the Reporting currency  */  
   Rpt3NettActivityAmt:number,
      /**  Price Per Unit in Document currency  */  
   DocPricePerUnit:number,
      /**  Price Per Unit in Report Currency 1  */  
   Rpt1PricePerUnit:number,
      /**  Price Per Unit in Report Currency 2  */  
   Rpt2PricePerUnit:number,
      /**  Price Per Unit in Report Currency 3  */  
   Rpt3PricePerUnit:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  */  
   ARInvoiceLine:number,
      /**  Tax Category ID  */  
   TaxCatID:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   MarkUpAmt:number,
   DocMarkUpAmt:number,
   Rpt1MarkUpAmt:number,
   Rpt2MarkUpAmt:number,
   Rpt3MarkUpAmt:number,
      /**  Phase Description  */  
   PhaseDescription:string,
   BitFlag:number,
   PBillSchDescription:string,
   PBSchWrkDescription:string,
   PBWrkMeasuredDtlDescription:string,
   PBWrkMeasuredHeadDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBGInvcDtlTCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Project ID.  */  
   ProjectID:string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.  */  
   InvoiceNum:number,
      /**  Sequence  */  
   InvoiceLine:number,
      /**   Identifies the type of line. The line types are:
MWA = Measured Work, LBD = Employee Labor (Direct Labor), LBC = Contract Labor, MTL = Material, SUB = Subcontract, MSC = Other Direct Cost  */  
   TranType:string,
      /**  File where transaction was from  */  
   TranFile:string,
      /**  Key to the actual source document  */  
   TranKey:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence of the Job that the labor transaction applies to  */  
   AssemblySeq:number,
      /**  Sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.  */  
   OprSeq:number,
      /**  Part Number  */  
   PartNum:string,
      /**  Material Sequence  */  
   MatNum:number,
      /**  Employee Number  */  
   EmployeeNum:string,
      /**  Role Code  */  
   RoleCd:string,
      /**   List of the values:PROJ = Project, EMPL = Employee,
ROLE = Role, LBR = Labor Details  */  
   LbrRateFrom:string,
      /**  Charge Rate  */  
   ChargeRate:number,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Purchase Order Number  */  
   PONum:number,
      /**  Purchase Order Line  */  
   POLine:number,
      /**  Purchase Order Release  */  
   PORelNum:number,
      /**  Packing Slip Line  */  
   PackLine:number,
      /**  Subcontract Amount  */  
   SubExtAmt:number,
      /**  subcontract mark up percent  */  
   PBSubMarkUp:number,
      /**  Subcontract Cost Markup Amount  */  
   SubMarkUpAmt:number,
      /**  Total Subcontract Amount  */  
   SubTotalAmt:number,
      /**  Hours  */  
   Hours:number,
      /**  Labor Amount  */  
   LbrExtAmt:number,
      /**  Labor Cost Markup percent  */  
   PBLbrMarkUp:number,
      /**  Labor Cost Amount  */  
   LbrMarkUpAmt:number,
      /**  Total Labor Amount  */  
   LbrTotalAmt:number,
      /**  Material Cost  */  
   MtlCost:number,
      /**  Material  Amount  */  
   MtlExtAmt:number,
      /**  Material mark up percent  */  
   PBMtlMarkUp:number,
      /**  Material Cost Amount  */  
   MtlMarkUpAmt:number,
      /**  Total Material Amount  */  
   MtlTotalAmt:number,
      /**  Total Ceiling  */  
   PBCeilingTotal:number,
      /**  Fee Ceiling  */  
   PBCeilingFee:number,
      /**  Other Cost Ceiling  */  
   PBCeilingMisc:number,
      /**  Burden Ceiling  */  
   PBCeilingBur:number,
      /**  Material Burden Ceiling  */  
   PBCeilingMtlBur:number,
      /**  Material Ceiling  */  
   PBCeilingMtl:number,
      /**  Subcontract Ceiling  */  
   PBCeilingSub:number,
      /**  Labor Ceiling  */  
   PBCeilingLbr:number,
      /**  Individual Ceilings on Suppliers  */  
   PBIndCeilingSup:boolean,
      /**  Individual Ceilings on Employee  */  
   PBIndCeilingEmp:boolean,
      /**  Individual Ceilings on Project Role  */  
   PBIndCeilingPRole:boolean,
      /**  Project Over Ceiling  */  
   OverCeilingPrj:number,
      /**  Fee Over Ceiling  */  
   OverCeilingFee:number,
      /**  Burden Over Ceiling  */  
   OverCeilingBur:number,
      /**  Other Cost Over Ceiling  */  
   OverCeilingMisc:number,
      /**  Subcontract Over Ceiling  */  
   OverCeilingSub:number,
      /**  Material Burden Over Ceiling  */  
   OverCeilingMtlBur:number,
      /**  Material Over Ceiling  */  
   OverCeilingMtl:number,
      /**  Labor Over Ceiling  */  
   OverCeilingLbr:number,
      /**  Retention Amount  */  
   RetentionAmt:number,
      /**  Retention Percentage  */  
   RetentionPrcnt:number,
      /**  Contract Labor  */  
   ContrLbr:boolean,
      /**  Transaction Quantity  */  
   TranQty:number,
      /**   Following options: PRJ = Project Price List,
CUS = Customer Price List, GEN = General Price List, TRN = Transaction  */  
   PriceFrom:string,
      /**  Transaction Type  */  
   PartTranType:string,
      /**  Reduced Line amount  */  
   CutLineAmt:number,
      /**  Over Ceiling  */  
   OverCeilingAmt:number,
      /**  Ceiling  */  
   CeilingAmt:number,
      /**  Ceiling comes From: RoleCd, Employee, Supplier  */  
   CeilingFrom:string,
      /**  Current Invoice Amount  */  
   CurrentInvoicedAmt:number,
      /**  ODC Amount  */  
   MiscExtAmt:number,
      /**  ODC markup percent. If Invoicing Type = CP then Copy of Project.PBMiscMarkUp  */  
   PBMiscMarkUp:number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100  */  
   MiscMarkUpAmt:number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt  */  
   MiscTotalAmt:number,
      /**  Misc Change ID for TM/CP Invoices  */  
   MiscCode:string,
      /**  Labor Invoiced Amount  */  
   LbrInvAmt:number,
      /**  Material Invoiced Amount  */  
   MtlInvAmt:number,
      /**  Subcontract Invoiced Amount  */  
   SubInvAmt:number,
      /**  Burden Invoiced Amount  */  
   BdnInvAmt:number,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   APInvoiceNum:string,
      /**  This field along with Company, VendorNum and APInvoiceNum make up the unique key to the APInvDtl table.  */  
   APInvoiceLine:number,
      /**  Subcontract labor  */  
   SubLbrAmt:number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts)  */  
   SubMtlAmt:number,
      /**  in the Project currency  */  
   DocLbrExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt1LbrExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt2LbrExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt3LbrExtAmt:number,
      /**  in the Project currency  */  
   DocLbrMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt1LbrMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt2LbrMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt3LbrMarkUpAmt:number,
      /**  in the Project currency  */  
   DocLbrTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt1LbrTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt2LbrTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt3LbrTotalAmt:number,
      /**  in the Project currency  */  
   DocMtlExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt1MtlExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt2MtlExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt3MtlExtAmt:number,
      /**  in the Project currency  */  
   DocMtlMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt1MtlMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt2MtlMarkUpAmt:number,
      /**  in the Reporting currency  */  
   Rpt3MtlMarkUpAmt:number,
      /**  in the Project currency  */  
   DocMtlTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt1MtlTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt2MtlTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt3MtlTotalAmt:number,
      /**  in the Project currency  */  
   DocSubExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt1SubExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt2SubExtAmt:number,
      /**  in the Reporting currency  */  
   Rpt3SubExtAmt:number,
      /**  Subcontract Cost Markup Amount  in the Project currency  */  
   DocSubMarkUpAmt:number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   Rpt1SubMarkUpAmt:number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   Rpt2SubMarkUpAmt:number,
      /**  Subcontract Cost Markup Amount  in the Reporting currency  */  
   Rpt3SubMarkUpAmt:number,
      /**  in the Project currency  */  
   DocSubTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt1SubTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt2SubTotalAmt:number,
      /**  in the Reporting currency  */  
   Rpt3SubTotalAmt:number,
      /**  ODC Amount in the Project currency  */  
   DocMiscExtAmt:number,
      /**  ODC Amount in the Reporting currency  */  
   Rpt1MiscExtAmt:number,
      /**  ODC Amount in the Reporting currency  */  
   Rpt2MiscExtAmt:number,
      /**  ODC Amount in the Reporting currency  */  
   Rpt3MiscExtAmt:number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Project currency  */  
   DocMiscMarkUpAmt:number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   Rpt1MiscMarkUpAmt:number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   Rpt2MiscMarkUpAmt:number,
      /**  If Invoicing Type = CP it?s MiscExtAmt * PBSubMarkUp /100 in the Reporting currency  */  
   Rpt3MiscMarkUpAmt:number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Project currency  */  
   DocMiscTotalAmt:number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   Rpt1MiscTotalAmt:number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   Rpt2MiscTotalAmt:number,
      /**  Total ODC Amount, If Invoicing Type = CP it is equal MiscAmt + MiscMarkUpAmt, Otherwise it is equal  MiscAmt
in the Reporting currency  */  
   Rpt3MiscTotalAmt:number,
      /**  in the Project currency  */  
   DocMtlCost:number,
      /**  in the Reporting currency  */  
   Rpt1MtlCost:number,
      /**  in the Reporting currency  */  
   Rpt2MtlCost:number,
      /**  in the Reporting currency  */  
   Rpt3MtlCost:number,
      /**  Reduced Line amount in the Project currency  */  
   DocCutLineAmt:number,
      /**  Reduced Line amount in the Reporting currency  */  
   Rpt1CutLineAmt:number,
      /**  Reduced Line amount in the Reporting currency  */  
   Rpt2CutLineAmt:number,
      /**  Reduced Line amount in the Reporting currency  */  
   Rpt3CutLineAmt:number,
      /**  Ceiling in the Project currency  */  
   DocCeilingAmt:number,
      /**  Ceiling in the Reporting currency  */  
   Rpt1CeilingAmt:number,
      /**  Ceiling in the Reporting currency  */  
   Rpt2CeilingAmt:number,
      /**  Ceiling in the Reporting currency  */  
   Rpt3CeilingAmt:number,
      /**  Over Ceiling in the Project currency  */  
   DocOverCeilingAmt:number,
      /**  Over Ceiling in the Reporting currency  */  
   Rpt1OverCeilingAmt:number,
      /**  Over Ceiling in the Reporting currency  */  
   Rpt2OverCeilingAmt:number,
      /**  Over Ceiling in the Reporting currency  */  
   Rpt3OverCeilingAmt:number,
      /**  in the Project currency  */  
   DocCurrentInvoicedAmt:number,
      /**  in the Reporting currency  */  
   Rpt1CurrentInvoicedAmt:number,
      /**  in the Reporting currency  */  
   Rpt2CurrentInvoicedAmt:number,
      /**  in the Reporting currency  */  
   Rpt3CurrentInvoicedAmt:number,
      /**  Labor Invoiced Amount in the Project currency  */  
   DocLbrInvAmt:number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   Rpt1LbrInvAmt:number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   Rpt2LbrInvAmt:number,
      /**  Labor Invoiced Amount in the Reporting currency  */  
   Rpt3LbrInvAmt:number,
      /**  Material Invoiced Amount in the Project currency  */  
   DocMtlInvAmt:number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   Rpt1MtlInvAmt:number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   Rpt2MtlInvAmt:number,
      /**  Material Invoiced Amount in the Reporting currency  */  
   Rpt3MtlInvAmt:number,
      /**  Subcontract Invoiced Amount in the Project currency  */  
   DocSubInvAmt:number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   Rpt1SubInvAmt:number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   Rpt2SubInvAmt:number,
      /**  Subcontract Invoiced Amount in the Reporting currency  */  
   Rpt3SubInvAmt:number,
      /**  Burden Invoiced Amount in the Project currency  */  
   DocBdnInvAmt:number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   Rpt1BdnInvAmt:number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   Rpt2BdnInvAmt:number,
      /**  Burden Invoiced Amount in the Reporting currency  */  
   Rpt3BdnInvAmt:number,
      /**  Subcontract labor in the Project currency  */  
   DocSubLbrAmt:number,
      /**  Subcontract labor in the Reporting currency  */  
   Rpt1SubLbrAmt:number,
      /**  Subcontract labor in the Reporting currency  */  
   Rpt2SubLbrAmt:number,
      /**  Subcontract labor in the Reporting currency  */  
   Rpt3SubLbrAmt:number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Project currency  */  
   DocSubMtlAmt:number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   Rpt1SubMtlAmt:number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   Rpt2SubMtlAmt:number,
      /**  Subcontract material Ientered in AP Invoice for PO subcontract receipts) in the Reporting currency  */  
   Rpt3SubMtlAmt:number,
      /**  Role Mark Up percentage  */  
   PBRoleMarkup:number,
      /**  reference to Pack Slip number  */  
   PackNum:string,
      /**  Charge Rate  */  
   DocChargeRate:number,
      /**  Charge Rate  */  
   Rpt1ChargeRate:number,
      /**  Charge Rate  */  
   Rpt2ChargeRate:number,
      /**  Charge Rate  */  
   Rpt3ChargeRate:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the InvcDtl table for the AR Invoice line which includes the amounts related to this PBGInvcDtl line  */  
   ARInvoiceLine:number,
      /**  in the Project currency  */  
   DocRetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt1RetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt2RetentionAmt:number,
      /**  in the Reporting currency  */  
   Rpt3RetentionAmt:number,
      /**  Field to be deleted in Invoice Review, means that the related transaction will be skipped in the Recalculation of the Invoice  */  
   ToDelete:boolean,
      /**  Flag indicated that the amount has been updated in the Invoice Review program  */  
   UpdatedAmt:boolean,
      /**  copy from LaborDtl.TimeTypCd  */  
   TimeTypCd:string,
      /**  Reference to the Parent Line from the Ceiling Line  */  
   ParentInvoiceLine:number,
      /**  Tax Category ID  */  
   TaxCatID:string,
      /**  Line Comment  */  
   Comment:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  OrderNum  */  
   OrderNum:number,
      /**  OrderLine  */  
   OrderLine:number,
      /**  OrderRelNum  */  
   OrderRelNum:number,
      /**  UOM  */  
   UOM:string,
      /**  PriceListCode  */  
   PriceListCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BreakListCode  */  
   BreakListCode:string,
   DspCPMarkUpAmt:number,
   DspCPMarkUpPrc:number,
   DspCPTotalAmt:number,
   DspLbrAssemblySeq:number,
   DspLbrJobNum:string,
   DspLbrOprSeq:number,
   DspMtlAssemblySeq:number,
   DspMtlJobNum:string,
   DspMtlOprSeq:number,
   DspSubAssemblySeq:number,
   DspSubJobNum:string,
   DspSubOprSeq:number,
      /**  Phase Description  */  
   PhaseDescription:string,
   Rpt1TotLineAmt:number,
   Rpt2TotLineAmt:number,
   Rpt3TotLineAmt:string,
   TotLineAmt:number,
   CurrencyCode:string,
   DocTotLineAmt:number,
   BitFlag:number,
   EmployeeNumName:string,
   MiscCodeDescription:string,
   PartNumPartDescription:string,
   RoleCdRoleDescription:string,
   TaxCatIDDescription:string,
   VendorNumName:string,
   VendorNumVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBGInvcHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Project ID.  */  
   ProjectID:string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  */  
   InvoiceNum:number,
      /**  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  */  
   TmpInvcNum:number,
      /**   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  */  
   ConInvMeth:string,
   DspProjectInvcNum:string,
      /**  Actual Invoice date  */  
   InvoiceDate:string,
   DspInvoiceNum:number,
   DspTempInvcNum:number,
      /**  Progress Billing - Order Number  */  
   PBOrderNum:number,
      /**  Progress Billing - Order Line  */  
   PBOrderLine:number,
      /**  A = Approved, P = Posted, empty - review  */  
   PrcStatus:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBGInvcHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Project ID.  */  
   ProjectID:string,
      /**  Actual invoice number. Zero means that invoice has not been generated yet.Negative is used only to relation Fixed Fee invoices if there are different SO data on the some processed Billing Schedules (as many different SO data as many different Invoices are generated)  */  
   InvoiceNum:number,
      /**  Temporary invoice number that will used to identify the data. Once the data is posted as an actual invoice then this number will be blanked out  */  
   TmpInvcNum:number,
      /**   ?CS? = Customer Shipment, ?MB? = Milestone Billing, ?FF? = Fixed Fee
?TM? = Time and Materials
?CP? = Cost Plus
?PP? = Progress Payments  */  
   ConInvMeth:string,
      /**  Contract Reference  */  
   ConReference:string,
      /**  Date the user entered in Invoice Preparation form  */  
   TmpInvcDate:string,
      /**  Actual Invoice date  */  
   InvoiceDate:string,
      /**  Currency Code of the Contract  */  
   CurrencyCode:string,
      /**  Rate Type Code  */  
   RateGrpCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  */  
   LockRate:boolean,
      /**  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  */  
   ExchangeRate:number,
      /**  P = Percentage, F = Fixed Amount  */  
   PBFeePrjType:string,
      /**  P = Percentage, F = Fixed Amount  */  
   PBFeeSubType:string,
      /**  P = Percentage, F = Fixed Amount  */  
   PBFeeMtlType:string,
      /**  P = Percentage, F = Fixed Amount  */  
   PBFeeLbrType:string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   PBFeePrjApply:string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   PBFeeSubApply:string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   PBFeeMtlApply:string,
      /**  F = First Invoice Only, A = All Invoices.  */  
   PBFeeLbrApply:string,
      /**  Project Fee Charge  */  
   PBFeePrjCharge:number,
      /**  Subcontract Fee Charge  */  
   PBFeeSubCharge:number,
      /**  Material Fee Charge  */  
   PBFeeMtlCharge:number,
      /**  Labor Fee Charge  */  
   PBFeeLbrCharge:number,
      /**  Burden Amount  */  
   BdnAmt:number,
      /**  Other Direct Coat Amount  */  
   MiscAmt:number,
      /**  Subcontract Amount  */  
   SubAmt:number,
      /**  Material Amount  */  
   MtlAmt:number,
      /**  Labor Amount  */  
   LbrAmt:number,
      /**  Total Fee  */  
   PBFeeTotal:number,
      /**  Project Fee Amount  */  
   PBFeePrjAmt:number,
      /**  Subcontract Fee Amount  */  
   PBFeeSubAmt:number,
      /**  Material Fee Amount  */  
   PBFeeMtlAmt:number,
      /**  Labor Fee Amount  */  
   PBFeeLbrAmt:number,
      /**  N = Net Cost, G = Gross Cost  */  
   PBFeeApplyOn:string,
      /**  Progress Billing - Order Number  */  
   PBOrderNum:number,
      /**  Progress Billing - Order Line  */  
   PBOrderLine:number,
      /**  The percentage to be retained, this can be 0.  */  
   RetentionPrcnt:number,
      /**  Retention Processing with a system list of options: M - Maximum of Contract Value, I - Invoice Value  */  
   RetentionProc:string,
      /**  Fee Retention Amount  */  
   PBFeeRetentionAmt:number,
      /**  Fee Nett Amount  */  
   PBFeeNettAmt:number,
      /**  Summa of elements amounts  */  
   InvcTotalSumAmt:number,
      /**  Total amount plus Fee  */  
   InvcAddFeeAmt:number,
      /**  Total reduced by Ceiling  */  
   InvcCutCeiling:number,
      /**  Total redused by Retention  */  
   InvcCutRetention:number,
      /**  Final Total Invoice  */  
   InvcTotal:number,
      /**  A = Approved, P = Posted, empty - review  */  
   PrcStatus:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Parameter of the Invoice Preparation process  */  
   PeriodEndDate:string,
      /**  Fee Ceiling  */  
   PBCeilingFee:number,
      /**  Total Ceiling  */  
   PBCeilingTotal:number,
      /**  Individual Ceilings on Suppliers  */  
   PBIndCeilingSup:boolean,
      /**  Individual Ceilings on Employee  */  
   PBIndCeilingEmp:boolean,
      /**  Individual Ceilings on Role  */  
   PBIndCeilingPRole:boolean,
      /**  OverCeiling Fees (negative)  */  
   OverCeilingFees:number,
      /**  OverCeilingTotalAmt  */  
   OverCeilingTotalAmt:number,
      /**  Retention Amount  */  
   RetentionAmt:number,
      /**  Percentage of Progress Payment, for PP invoice only.  */  
   PPAllowPcnt:number,
      /**  Date the invoice was approved for posting  */  
   ApprovedDate:string,
      /**  Approved by user id  */  
   ApprovedBy:string,
      /**  in the Project currency  */  
   DocPBFeeLbrCharge:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeLbrCharge:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeLbrCharge:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeLbrCharge:number,
      /**  in the Project currency  */  
   DocPBFeeLbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeLbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeLbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeLbrAmt:number,
      /**  in the Project currency  */  
   DocPBFeeMtlCharge:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeMtlCharge:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeMtlCharge:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeMtlCharge:number,
      /**  in the Project currency  */  
   DocPBFeeMtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeMtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeMtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeMtlAmt:number,
      /**  in the Project currency  */  
   DocPBFeeSubCharge:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeSubCharge:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeSubCharge:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeSubCharge:number,
      /**  in the Project currency  */  
   DocPBFeeSubAmt:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeSubAmt:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeSubAmt:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeSubAmt:number,
      /**  in the Project currency  */  
   DocPBFeePrjCharge:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeePrjCharge:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeePrjCharge:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeePrjCharge:number,
      /**  in the Project currency  */  
   DocPBFeeTotal:number,
      /**  in the Reporting currency  */  
   Rpt1PBFeeTotal:number,
      /**  in the Reporting currency  */  
   Rpt2PBFeeTotal:number,
      /**  in the Reporting currency  */  
   Rpt3PBFeeTotal:number,
      /**  in the Project currency  */  
   DocLbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt1LbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt2LbrAmt:number,
      /**  in the Reporting currency  */  
   Rpt3LbrAmt:number,
      /**  in the Project currency  */  
   DocMtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt1MtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt2MtlAmt:number,
      /**  in the Reporting currency  */  
   Rpt3MtlAmt:number,
      /**  in the Project currency  */  
   DocSubAmt:number,
      /**  in the Reporting currency  */  
   Rpt1SubAmt:number,
      /**  in the Reporting currency  */  
   Rpt2SubAmt:number,
      /**  in the Reporting currency  */  
   Rpt3SubAmt:number,
      /**  in the Project currency  */  
   DocBdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt1BdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt2BdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt3BdnAmt:number,
      /**  in the Project currency  */  
   DocMiscAmt:number,
      /**  in the Reporting currency  */  
   Rpt1MiscAmt:number,
      /**  in the Reporting currency  */  
   Rpt2MiscAmt:number,
      /**  in the Reporting currency  */  
   Rpt3MiscAmt:number,
      /**  Fee Ceiling in the Project currency  */  
   DocPBCeilingFee:number,
      /**  Fee Ceiling in the Reporting currency  */  
   Rpt1PBCeilingFee:number,
      /**  Fee Ceiling in the Reporting currency  */  
   Rpt2PBCeilingFee:number,
      /**  Fee Ceiling in the Reporting currency  */  
   Rpt3PBCeilingFee:number,
      /**  in the Project currency  */  
   DocPBCeilingTotal:number,
      /**  in the Reporting currency  */  
   Rpt1PBCeilingTotal:number,
      /**  in the Reporting currency  */  
   Rpt2PBCeilingTotal:number,
      /**  in the Reporting currency  */  
   Rpt3PBCeilingTotal:number,
      /**  OverCeiling Fees (negative) in the Project currency  */  
   DocOverCeilingFees:number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   Rpt1OverCeilingFees:number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   Rpt2OverCeilingFees:number,
      /**  OverCeiling Fees (negative) in the Reporting currency  */  
   Rpt3OverCeilingFees:number,
      /**  Retention Amount in the Project currency  */  
   DocRetentionAmt:number,
      /**  Retention Amount in the Reporting currency  */  
   Rpt1RetentionAmt:number,
      /**  Retention Amount in the Reporting currency  */  
   Rpt2RetentionAmt:number,
      /**  Retention Amount in the Reporting currency  */  
   Rpt3RetentionAmt:number,
      /**  OverCeilingTotalAmt in the Project currency  */  
   DocOverCeilingTotalAmt:number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   Rpt1OverCeilingTotalAmt:number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   Rpt2OverCeilingTotalAmt:number,
      /**  OverCeilingTotalAmt in the Reporting currency  */  
   Rpt3OverCeilingTotalAmt:number,
      /**  Fee Retention Amount in the Project currency  */  
   DocPBFeeRetentionAmt:number,
      /**  Fee Retention Amount in the Reporting currency  */  
   Rpt1PBFeeRetentionAmt:number,
      /**  Fee Retention Amount in the Reporting currency  */  
   Rpt2PBFeeRetentionAmt:number,
      /**  Fee Retention Amount in the Reporting currency  */  
   Rpt3PBFeeRetentionAmt:number,
      /**  Fee Nett Amount in the Project currency  */  
   DocPBFeeNettAmt:number,
      /**  Fee Nett Amount in the Reporting currency  */  
   Rpt1PBFeeNettAmt:number,
      /**  Fee Nett Amount in the Reporting currency  */  
   Rpt2PBFeeNettAmt:number,
      /**  Fee Nett Amount in the Reporting currency  */  
   Rpt3PBFeeNettAmt:number,
      /**  Summa of elements amounts  in the Project currency  */  
   DocInvcTotalSumAmt:number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   Rpt1InvcTotalSumAmt:number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   Rpt2InvcTotalSumAmt:number,
      /**  Summa of elements amounts  in the Reporting currency  */  
   Rpt3InvcTotalSumAmt:number,
      /**  Total amount plus Fee in the Project currency  */  
   DocInvcAddFeeAmt:number,
      /**  Total amount plus Fee in the Reporting currency  */  
   Rpt1InvcAddFeeAmt:number,
      /**  Total amount plus Fee in the Reporting currency  */  
   Rpt2InvcAddFeeAmt:number,
      /**  Total amount plus Fee in the Reporting currency  */  
   Rpt3InvcAddFeeAmt:number,
      /**  Total reduced by Ceiling in the Project currency  */  
   DocInvcCutCeiling:number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   Rpt1InvcCutCeiling:number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   Rpt2InvcCutCeiling:number,
      /**  Total reduced by Ceiling in the Reporting currency  */  
   Rpt3InvcCutCeiling:number,
      /**  Final Total Invoice in the Project currency  */  
   DocInvcTotal:number,
      /**  Final Total Invoice in the Reporting currency  */  
   Rpt1InvcTotal:number,
      /**  Final Total Invoice in the Reporting currency  */  
   Rpt2InvcTotal:number,
      /**  Final Total Invoice in the Reporting currency  */  
   Rpt3InvcTotal:number,
      /**  Labor actual amount  */  
   SumLbrTotalAmt:number,
      /**  Material actual amount  */  
   SumMtlTotalAmt:number,
      /**  Subcontract actual amount  */  
   SumSubTotalAmt:number,
      /**  Burden actual amount  */  
   SumBdnAmt:number,
      /**  Labor actual amount in the Project currency  */  
   DocSumLbrTotalAmt:number,
      /**  Labor actual amount in the Reporting currency  */  
   Rpt1SumLbrTotalAmt:number,
      /**  Labor actual amount in the Reporting currency  */  
   Rpt2SumLbrTotalAmt:number,
      /**  Labor actual amount in the Reporting currency  */  
   Rpt3SumLbrTotalAmt:number,
      /**  Material actual amount in the Project currency  */  
   DocSumMtlTotalAmt:number,
      /**  Material actual amount in the Reporting currency  */  
   Rpt1SumMtlTotalAmt:number,
      /**  Material actual amount in the Reporting currency  */  
   Rpt2SumMtlTotalAmt:number,
      /**  Material actual amount in the Reporting currency  */  
   Rpt3SumMtlTotalAmt:number,
      /**  Subcontract actual amount in the Project currency  */  
   DocSumSubTotalAmt:number,
      /**  Subcontract actual amount in the Reporting currency  */  
   Rpt1SumSubTotalAmt:number,
      /**  Subcontract actual amount in the Reporting currency  */  
   Rpt2SumSubTotalAmt:number,
      /**  Subcontract actual amount in the Reporting currency  */  
   Rpt3SumSubTotalAmt:number,
      /**  in the Project currency  */  
   DocSumBdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt1SumBdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt2SumBdnAmt:number,
      /**  in the Reporting currency  */  
   Rpt3SumBdnAmt:number,
      /**  Project Fee Amount in Document Currency  */  
   DocPBFeePrjAmt:number,
      /**  Project Fee Amount in Report Currency 1  */  
   Rpt1PBFeePrjAmt:number,
      /**  Project Fee Amount in Report Currency 2  */  
   Rpt2PBFeePrjAmt:number,
      /**  Project Fee Amount in Report Currency 3  */  
   Rpt3PBFeePrjAmt:number,
      /**   Other Direct Cost Fee Type
List of options: P = Percentage, F = Fixed Amount  */  
   PBFeeMiscType:string,
      /**   Other Direct Cost Fee Apply Type
List of options: F = First Invoice Only, A = All Invoices.  */  
   PBFeeMiscApply:string,
      /**  Other Direct Cost Fee value being applied  */  
   PBFeeMiscCharge:number,
      /**  Calculated ODC Fee amount  */  
   PBFeeMiscAmt:number,
      /**  Other Direct Cost Fee value being applied in the Project currency  */  
   DocPBFeeMiscCharge:number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   Rpt1PBFeeMiscCharge:number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   Rpt2PBFeeMiscCharge:number,
      /**  Other Direct Cost Fee value being applied in the Reporting currency  */  
   Rpt3PBFeeMiscCharge:number,
      /**  Calculated ODC Fee amount in the Project currency  */  
   DocPBFeeMiscAmt:number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   Rpt1PBFeeMiscAmt:number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   Rpt2PBFeeMiscAmt:number,
      /**  Calculated ODC Fee amount in the Reporting currency  */  
   Rpt3PBFeeMiscAmt:number,
      /**  Retention percentage. How this is used is dependent on RetentionProc field.  */  
   PBRetentionPcnt:number,
      /**  Flag indicated that one of its lines has been updated or deleted in the Invoice Review program  */  
   Updated:boolean,
      /**  Indicates if invoice should be auto printed  */  
   AutoPrint:boolean,
      /**  Fee Invoice Text  */  
   PBFeeInvoiceText:string,
      /**  Comment  */  
   Comment:string,
      /**  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  */  
   PPAllOrderLines:boolean,
      /**  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  */  
   PPAllPrjJobs:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag indicates if AR invoices are allowed to be generated even if the element is over the predefined ceiling (limit), also indicates if the invoice amount should stay limited or not when ceiling exists. It is copied from the current value of Project flag  */  
   ConOverCeiling:boolean,
   AutoPrintReady:boolean,
      /**  Base Currency ID  */  
   BaseCurrencyID:string,
   DspInvoiceNum:number,
   DspTempInvcNum:number,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CustNumName:string,
   CustNumCustID:string,
   ProjectIDConReference:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBGInvoiceListTableset{
   PBGInvcHeadList:Erp_Tablesets_PBGInvcHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PBGInvoiceTableset{
   PBGInvcHead:Erp_Tablesets_PBGInvcHeadRow[],
   PBGInvcBdn:Erp_Tablesets_PBGInvcBdnRow[],
   PBGInvcDtlFF:Erp_Tablesets_PBGInvcDtlFFRow[],
   PBGInvcDtlTC:Erp_Tablesets_PBGInvcDtlTCRow[],
   PBInvoicedAmt:Erp_Tablesets_PBInvoicedAmtRow[],
   PBPrjInvcPhaseList:Erp_Tablesets_PBPrjInvcPhaseListRow[],
   PBProjectsList:Erp_Tablesets_PBProjectsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PBInvoicedAmtRow{
      /**  Company  */  
   Company:string,
      /**  Project ID  */  
   ProjectID:string,
      /**  Related To File  */  
   RelatedToFile:string,
      /**  Transaction Key  */  
   TranKey:string,
      /**  Amount strored by Invoice Preparation before Posting ,used to appropriate compare with Ceiling  */  
   DocPrepAmt:number,
      /**  Preparation over ceiling in Base curency  */  
   PrepOverCeiling:number,
      /**  Preparation over ceiling in Document curency  */  
   DocPrepOverCeiling:number,
      /**  Generated Over ceiling in Base currency  */  
   GenOverCeiling:number,
      /**  Generated Over ceiling in Document currency  */  
   DocGenOverCeiling:number,
      /**  Posted Over Ceiling in Base currency  */  
   PostOverCeiling:number,
      /**  Posted Over Ceiling in Document currency  */  
   DocPostOverCeiling:number,
      /**  Ceiling Generated Consumed in Base currency  */  
   GenAmt:number,
      /**  Ceiling Generated Consumed in Document currency  */  
   DocGenAmt:number,
      /**  Ceiling Posted Consumed in Base currency  */  
   PostAmt:number,
      /**  Ceiling Posted Consumed in Document currency  */  
   DocPostAmt:number,
      /**  Ceiling Preparation Consumed in Document currency  */  
   PrepAmt:number,
      /**  Ceiling Limit in Base currency  */  
   CeilingLimit:number,
      /**  Ceiling Limit in Project Currency  */  
   DocCeilingLimit:number,
      /**  Invoice Number. It's zero for preparation and total values for whole project  */  
   InvoiceNum:number,
      /**  Tax Category ID  */  
   TaxCatID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBPrjInvcPhaseListRow{
   Company:string,
   ProjectID:string,
   InvoiceNum:number,
   PhaseID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PBProjectsListRow{
   Company:string,
   ProjectID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPBGInvoiceTableset{
   PBGInvcHead:Erp_Tablesets_PBGInvcHeadRow[],
   PBGInvcBdn:Erp_Tablesets_PBGInvcBdnRow[],
   PBGInvcDtlFF:Erp_Tablesets_PBGInvcDtlFFRow[],
   PBGInvcDtlTC:Erp_Tablesets_PBGInvcDtlTCRow[],
   PBInvoicedAmt:Erp_Tablesets_PBInvoicedAmtRow[],
   PBPrjInvcPhaseList:Erp_Tablesets_PBPrjInvcPhaseListRow[],
   PBProjectsList:Erp_Tablesets_PBProjectsListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param projectID
      @param invoiceNum
   */  
export interface GetByID_input{
   projectID:string,
   invoiceNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PBGInvoiceTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PBGInvoiceTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PBGInvoiceTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ipProjectID
      @param ipConInvMeth
   */  
export interface GetDataByProjectID_input{
      /**  The ProjectID.  */  
   ipProjectID:string,
      /**  The ConInvMeth.  */  
   ipConInvMeth:string,
}

export interface GetDataByProjectID_output{
   returnObj:Erp_Tablesets_PBGInvoiceTableset[],
}

   /** Required : 
      @param ipProjectID
      @param ipConInvMeth
      @param ipInvoiceNum
   */  
export interface GetDataByTempInvoiceNum_input{
      /**  The ProjectID.  */  
   ipProjectID:string,
      /**  The ConInvMeth.  */  
   ipConInvMeth:string,
      /**  The Invoice Num.  */  
   ipInvoiceNum:number,
}

export interface GetDataByTempInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   opInvoiceNum:number,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PBGInvoiceListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param projectID
      @param invoiceNum
      @param recSeq
      @param bdnSetID
   */  
export interface GetNewPBGInvcBdn_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
   projectID:string,
   invoiceNum:number,
   recSeq:number,
   bdnSetID:string,
}

export interface GetNewPBGInvcBdn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param ds
      @param projectID
      @param invoiceNum
   */  
export interface GetNewPBGInvcDtlFF_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
   projectID:string,
   invoiceNum:number,
}

export interface GetNewPBGInvcDtlFF_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param ds
      @param projectID
      @param invoiceNum
   */  
export interface GetNewPBGInvcDtlTC_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
   projectID:string,
   invoiceNum:number,
}

export interface GetNewPBGInvcDtlTC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param ds
      @param projectID
   */  
export interface GetNewPBGInvcHead_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
   projectID:string,
}

export interface GetNewPBGInvcHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param ds
      @param projectID
      @param invoiceNum
      @param relatedToFile
      @param tranKey
   */  
export interface GetNewPBInvoicedAmt_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
   projectID:string,
   invoiceNum:number,
   relatedToFile:string,
   tranKey:string,
}

export interface GetNewPBInvoicedAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

   /** Required : 
      @param whereClausePBGInvcHead
      @param whereClausePBGInvcBdn
      @param whereClausePBGInvcDtlFF
      @param whereClausePBGInvcDtlTC
      @param whereClausePBInvoicedAmt
      @param whereClausePBPrjInvcPhaseList
      @param whereClausePBProjectsList
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePBGInvcHead:string,
   whereClausePBGInvcBdn:string,
   whereClausePBGInvcDtlFF:string,
   whereClausePBGInvcDtlTC:string,
   whereClausePBInvoicedAmt:string,
   whereClausePBPrjInvcPhaseList:string,
   whereClausePBProjectsList:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PBGInvoiceTableset[],
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPBGInvoiceTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPBGInvoiceTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PBGInvoiceTableset[],
}
}

