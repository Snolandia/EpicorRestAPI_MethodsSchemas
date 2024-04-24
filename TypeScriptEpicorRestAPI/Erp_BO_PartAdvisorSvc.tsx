import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartAdvisorSvc
// Description: Part Advisor DataSet
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/$metadata", {
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
   Description: Get PartAdvisors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAdvisors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRow
   */  
export function get_PartAdvisors(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartAdvisor item
   Description: Calls GetByID to retrieve the PartAdvisor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAdvisor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartRow
   */  
export function get_PartAdvisors_Company_PartNum(Company:string, PartNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PartAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttchRow
   */  
export function get_PartAdvisors_Company_PartNum_PartAttches(Company:string, PartNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")/PartAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartAttch item
   Description: Calls GetByID to retrieve the PartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAttchRow
   */  
export function get_PartAdvisors_Company_PartNum_PartAttches_Company_PartNum_DrawingSeq(Company:string, PartNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")/PartAttches(" + Company + "," + PartNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttchRow
   */  
export function get_PartAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartAttch item
   Description: Calls GetByID to retrieve the PartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAttchRow
   */  
export function get_PartAttches_Company_PartNum_DrawingSeq(Company:string, PartNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAttches(" + Company + "," + PartNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InvcDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtlPAs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlPARow
   */  
export function get_InvcDtlPAs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/InvcDtlPAs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InvcDtlPA item
   Description: Calls GetByID to retrieve the InvcDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtlPA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlPARow
   */  
export function get_InvcDtlPAs_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/InvcDtlPAs(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcDtlPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get JobHeadPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobHeadPAs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadPARow
   */  
export function get_JobHeadPAs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/JobHeadPAs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JobHeadPA item
   Description: Calls GetByID to retrieve the JobHeadPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobHeadPA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobHeadPARow
   */  
export function get_JobHeadPAs_Company_JobNum(Company:string, JobNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobHeadPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/JobHeadPAs(" + Company + "," + JobNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JobHeadPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get OrderDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtlPAs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlPARow
   */  
export function get_OrderDtlPAs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/OrderDtlPAs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the OrderDtlPA item
   Description: Calls GetByID to retrieve the OrderDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtlPA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderDtlPARow
   */  
export function get_OrderDtlPAs_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/OrderDtlPAs(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderDtlPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartBins
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartBinRow
   */  
export function get_PartBins(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartBins", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartBin item
   Description: Calls GetByID to retrieve the PartBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartBin
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartBinRow
   */  
export function get_PartBins_Company_PartNum_WarehouseCode_BinNum_DimCode_LotNum_PCID_AttributeSetID(Company:string, PartNum:string, WarehouseCode:string, BinNum:string, DimCode:string, LotNum:string, PCID:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartBinRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartBins(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + DimCode + "," + LotNum + "," + PCID + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartBinRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlPAs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlPARow
   */  
export function get_QuoteDtlPAs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/QuoteDtlPAs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlPARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuoteDtlPA item
   Description: Calls GetByID to retrieve the QuoteDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlPA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlPARow
   */  
export function get_QuoteDtlPAs_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlPARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/QuoteDtlPAs(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlPARow)
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow)
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
   Description: This method returns a list of Parts
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: This method returns a dataset for Part Advisor
   OperationID: GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetByID", {
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
   Summary: Invoke method GetList
   Description: This method returns a list of Part, including those with blank Company ID
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetList", {
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
   Summary: Invoke method AfterGetRows
   OperationID: AfterGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AfterGetRows(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/AfterGetRows", {
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
   Summary: Invoke method AllowProfitability
   Description: Allows profitability
   OperationID: AllowProfitability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowProfitability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowProfitability(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/AllowProfitability", {
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
   Summary: Invoke method GetByIDWithCounters
   Description: This method returns a dataset for Part Advisor with counters
   OperationID: GetByIDWithCounters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDWithCounters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDWithCounters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDWithCounters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetByIDWithCounters", {
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
   Summary: Invoke method GetInvcDtlPARows
   Description: Searches and fills the InvcDtlPA table with the InvcDtl records that match the given part and the InvoiceType = SHP
   OperationID: GetInvcDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcDtlPARows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetInvcDtlPARows", {
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
   Summary: Invoke method GetInvcDtlPAList
   Description: Searches and fills the InvcDtlPA table with the InvcDtl records that match the given part and the InvoiceType = SHP
   OperationID: GetInvcDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcDtlPAList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetInvcDtlPAList", {
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
   Summary: Invoke method GetJobHeadPARows
   Description: Searches and fills the JobHeadPA table with the JobHead records that match the given part
   OperationID: GetJobHeadPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobHeadPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobHeadPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobHeadPARows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetJobHeadPARows", {
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
   Summary: Invoke method GetJobHeadPAList
   Description: Searches and fills the JobHeadPA table with the JobHead records that match the given part
   OperationID: GetJobHeadPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobHeadPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobHeadPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobHeadPAList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetJobHeadPAList", {
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
   Summary: Invoke method GetOrderDtlPARows
   Description: Searches and fills the OrderDtlPA table with the OrderDtl records that match the given part
   OperationID: GetOrderDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderDtlPARows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetOrderDtlPARows", {
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
   Summary: Invoke method GetOrderDtlPAList
   Description: Searches and fills the OrderDtlPA table with the OrderDtl records that match the given part
   OperationID: GetOrderDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderDtlPAList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetOrderDtlPAList", {
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
   Summary: Invoke method GetPartBinRows
   Description: Searches and fills the PartBin table with the PartBin records that match the given part
   OperationID: GetPartBinRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartBinRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetPartBinRows", {
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
   Summary: Invoke method GetPartBinList
   Description: Searches and fills the PartBin table with the PartBin records that match the given part
   OperationID: GetPartBinList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartBinList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetPartBinList", {
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
   Summary: Invoke method GetPartDetails
   Description: This method returns a list of Parts, including those with blank Company ID
   OperationID: GetPartDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetPartDetails", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetQuoteDtlPARows
   Description: Searches and fills the QuoteDtlPA table with the QuoteDtl records that match the given part
   OperationID: GetQuoteDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteDtlPARows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetQuoteDtlPARows", {
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
   Summary: Invoke method GetQuoteDtlPAList
   Description: Searches and fills the QuoteDtlPA table with the QuoteDtl records that match the given part
   OperationID: GetQuoteDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuoteDtlPAList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/GetQuoteDtlPAList", {
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
   Summary: Invoke method FindPart
   Description: This method finds the actual part number for the entered part and indicates if multiple actual parts match the entered part
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/FindPart", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlPARow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlPARow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadPARow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadPARow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlPARow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderDtlPARow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartBinRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartBinRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlPARow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlPARow[],
}

export interface Erp_Tablesets_InvcDtlPARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   "XRevisionNum":string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   "PartNum":string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   "LineDesc":string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   "IUM":string,
      /**  Our Current Revision Number for this Part.  */  
   "RevisionNum":string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   "POLine":string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   "TaxCatID":string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   "Commissionable":boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   "DiscountPercent":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   "OurOrderQty":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   "ProdCode":string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "OurShipQty":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  The packing slip line number that is being invoiced.  */  
   "PackLine":number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   "OrderNum":number,
      /**  The associated sales order line number.  */  
   "OrderLine":number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   "OrderRelNum":number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   "ShipToNum":string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   "ShipDate":string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   "ShipViaCode":string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "AdvanceBillCredit":number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "DocAdvanceBillCredit":number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   "CustNum":number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   "InvoiceComment":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   "ShpConNum":number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlBurUnitCost":number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   "COSPostingReqd":boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPosted":boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   "CallCode":string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   "RMALine":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   "JournalCode":string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   "SellingOrderQty":number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "SellingShipQty":number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   "ProjectID":string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   "MilestoneID":string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   "ListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   "OrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   "DocOrdBasedPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Sales representative commission rate.  */  
   "RepRate1":number,
      /**  Sales representative commission rate.  */  
   "RepRate2":number,
      /**  Sales representative commission rate.  */  
   "RepRate3":number,
      /**  Sales representative commission rate.  */  
   "RepRate4":number,
      /**  Sales representative commission rate.  */  
   "RepRate5":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit1":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit2":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit3":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit4":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit5":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Sales representative commission rate.  */  
   "RepRate":number,
   "RepSplit":number,
   "InvcHeadInvoiceDate":string,
   "InvcHeadCurrencyCode":string,
   "InvcHeadCustID":string,
   "InvcHeadCustName":string,
   "TotalCost":number,
   "ProfitLoss":number,
   "ProfitLossPct":number,
   "CustomerCustID":string,
   "CustomerName":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobHeadPARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff2":boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff3":boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff4":boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff5":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   "SchedStatus":string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The date that APS updated this record.  If this field is set then APS has scheduled the Job.  */  
   "APSUpdatedDate":string,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  The time, in decimal hours, that APS updated the dates and times for this job.  This field is only valid if the APSUpdateDate field is set.  */  
   "APSUpdatedTime":number,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Indicates that the quantity on this job is locked  */  
   "LockQty":boolean,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   "ProcessMode":string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   "PlannedActionDate":string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   "PlannedKitDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "EstTotalCost":number,
   "ActualTotalCost":number,
   "TotalVariance":number,
   "EstLabor":number,
   "EstBurden":number,
   "EstMaterial":number,
   "EstMtlBurden":number,
   "EstSubcontract":number,
   "ActLabor":number,
   "ActBurden":number,
   "ActMaterial":number,
   "ActMtlBurden":number,
   "ActSubcontract":number,
   "VarLabor":number,
   "VarBurden":number,
   "VarMaterial":number,
   "VarMtlBurden":number,
   "VarSubcontract":number,
   "EstSetupHrs":number,
   "ActSetupHrs":number,
   "EstProdHrs":number,
   "ActProdHrs":number,
   "EstTotalHrs":number,
   "ActTotalHrs":number,
   "VarTotalHrs":number,
   "JobAsmblAssemblySeq":number,
   "JobAsmblEstUnitCost":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OrderDtlPARow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidLine":boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   "Commissionable":boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   "OrderQty":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDiscount":number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   "RequestDate":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   "ShipComment":string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   "PickListComment":string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   "TaxCatID":string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   "AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "DocAdvanceBillBal":number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   "QuoteLine":number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   "TMBilling":boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   "OrigWhyNoTax":string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   "NeedByDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   "CustNum":number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   "Rework":boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   "RMANum":number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   "RMALine":number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   "SellingQuantity":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   "ShipLineComplete":boolean,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  Indicates if the price of the order line can be changed.  */  
   "LockPrice":boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate1":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate2":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate3":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate4":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate5":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit1":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit2":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit3":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit4":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit5":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OrderHedOrderDate":string,
   "OrderHedPONum":string,
   "CustomerCustID":string,
   "CustomerCustName":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Phase_c":string,
   "ItemID_c":string,
   "TypeCode_c":string,
   "OrigTypeCode_c":string,
   "PhaseID_c":string,
   "SalesCatID_c":string,
   "IndustryShipDate_c":string,
   "CreateDate_c":string,
   "PriceUpdateDate_c":string,
   "CreatedBy_c":string,
   "UpdatedBy_c":string,
}

export interface Erp_Tablesets_PartAttchRow{
   "Company":string,
   "PartNum":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartBinRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Identifies the Part Number. It must be valid in the Part table.  */  
   "PartNum":string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   "BinNum":string,
      /**   Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.
Note: With 9.0 the OnHandQty value is in terms of unit of measure (PartBin.DimCode) and does not require any conversion displaying in that uom.  */  
   "OnhandQty":number,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   "DimCode":string,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock and of the open job material requirements that are to be issued from stock (JobMtl.Buyit = No) for this Part within a specific bin within the warehouse.  NOTE: This value is the TOTAL of job allocation PartAlloc.  */  
   "AllocatedQty":number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled by stock in this bin in this warehouse and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   "SalesAllocatedQty":number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickingQty":number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   "SalesPickedQty":number,
      /**  New in 9.00.  Summary of mfg demands on firm jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobHead.Released = No.  */  
   "JobAllocatedQty":number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   "JobPickingQty":number,
      /**  Stock Quantity picked for jobs.  */  
   "JobPickedQty":number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Bin in this Warehouse.  */  
   "TFOrdAllocatedQty":number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   "TFOrdPickingQty":number,
      /**  Stock Quantity picked for transfer orders.  */  
   "TFOrdPickedQty":number,
      /**  Holds the Quantity in the Shipping process in the warehouse from this specific bin location.  */  
   "ShippingQty":number,
      /**  Amount in Bin that is in a Packaging Unit.  */  
   "PackedQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  Determines if the PartBin has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   "CountedDate":string,
      /**  When tracking inventory attributes this is the quantity per piece in the inventory UOM used to calculate Nbr. Of Pieces.  */  
   "QtyPerPiece":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "DimCodeDimCodeDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   "ClassID":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   "PUM":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "TrackDimension":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  */  
   "QtyBearing":boolean,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotBatch":boolean,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgBatch":boolean,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgLot":boolean,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotHeat":boolean,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotFirmware":boolean,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotBeforeDt":boolean,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgDt":boolean,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotCureDt":boolean,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotExpDt":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBatch":string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgBatch":string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgLot":string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttHeat":string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttFirmware":string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBeforeDt":string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgDt":string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttCureDt":string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttExpDt":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "TrackInventoryAttributes":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "DefaultAttributeSetID":number,
      /**  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  */  
   "HasMRPPlanningAttribute":boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   "ClassID":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   "PUM":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.


Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   "PurchasingFactor":number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PricePerCode":string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   "InternalUnitPrice":number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   "InternalPricePerCode":string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   "MfgComment":string,
      /**   Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   "PurComment":string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   "CostMethod":string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar1Label
is non blank.  */  
   "UserChar1":string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar2Label
is non blank.  */  
   "UserChar2":string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar3Label
is non blank.  */  
   "UserChar3":string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar4Label
is non blank.  */  
   "UserChar4":string,
      /**   User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate1Label
is non blank.  */  
   "UserDate1":string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate2Label is non blank.  */  
   "UserDate2":string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate3 Label is non blank.  */  
   "UserDate3":string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate4 Label is non blank.  */  
   "UserDate4":string,
      /**   User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec1Label
is non blank.  */  
   "UserDecimal1":number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec2Label is non blank.  */  
   "UserDecimal2":number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec3Label is non blank.  */  
   "UserDecimal3":number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec4Label is non blank.  */  
   "UserDecimal4":number,
      /**  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt1Label is non blank.  */  
   "UserInteger1":number,
      /**  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt2Label is non blank.  */  
   "UserInteger2":number,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   "LowLevelCode":number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "TrackDimension":boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DefaultDim":string,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   "CommodityCode":string,
      /**  Unique code for the Warranty for this part  */  
   "WarrantyCode":string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**  The Part's Unit Net Weight.  */  
   "NetWeight":number,
      /**  if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   "UsePartRev":boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   "PartsPerContainer":number,
      /**  Part's length.  */  
   "PartLength":number,
      /**  Part's width.  */  
   "PartWidth":number,
      /**  Part's Height.  */  
   "PartHeight":number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   "LotShelfLife":number,
      /**  This is a Web saleable part  */  
   "WebPart":boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   "RunOut":boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   "SubPart":string,
      /**  Part's diameter.  */  
   "Diameter":number,
      /**  Part's gravity.  */  
   "Gravity":number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   "OnHoldDate":string,
      /**  The Reason.Code associate with the reason why the part has been placed on hold. Valid only when Part.OnHold = Yes.  */  
   "OnHoldReasonCode":string,
      /**  Default analysis code to be used when this part appears as an assembly  on a quote or a job.  */  
   "AnalysisCode":string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   "GlobalPart":boolean,
      /**  MtlAnalysisCode  */  
   "MtlAnalysisCode":string,
      /**  Disables this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   "ISSuppUnitsFactor":number,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   "ImageFileName":string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   "ISOrigCountry":string,
      /**  Current setting for the prefix that will be attached to all new Serial Numbers as they are generated.  */  
   "SNPrefix":string,
      /**  Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999  */  
   "SNFormat":string,
      /**  Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer  */  
   "SNBaseDataType":string,
      /**  Used by the scheduling process when a part is stocked.  When TRUE,  the availability of this Part must be calculated via the TimePhase process prior to scheduling a Job.  */  
   "Constrained":boolean,
      /**  UPS / UCC Code required by some industries.  */  
   "UPCCode1":string,
      /**  UPS / UCC Code required by some industries.  */  
   "UPCCode2":string,
      /**  UPS / UCC Code required by some industries.  */  
   "UPCCode3":string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  For Customer Connect Only.  This field is used in Store Front to indicate if the part is available in stock.  */  
   "WebInStock":boolean,
      /**  Should this Part be included in Consolidated Purchasing?  */  
   "ConsolidatedPurchasing":boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**   Receiving Documents Required.
Indicates receiving documents are required when receiving this part.  This pertains only to lot tracked parts that are received to inventory. If checked, then at the time of receiving the system will require that one or more attachments with a reference to a DocType having Receipt = yes be entered.Requires DocManagement license.  */  
   "RecDocReq":boolean,
      /**  Maximum daily production value.  Used in demand shipping schedule.  */  
   "MDPV":number,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part. Pertains to Inventory shipments of lot tracked parts or shipments directly from the job only. If checked, then at the time of shipping the system will require that the PartLot.Ship DocsAvail, or JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   "ShipDocReq":boolean,
      /**  The returnable container for this part when the part needs to be returned.  The value is provided by the trading partner.  */  
   "ReturnableContainer":string,
      /**  The Part's Net Volume.  */  
   "NetVolume":number,
      /**  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  */  
   "QtyBearing":boolean,
      /**  This field contains the Country of Origin Code from the Country table.  For International shipping.  */  
   "NAFTAOrigCountry":string,
      /**  NAFTA Producer Code - For international shipping  */  
   "NAFTAProd":string,
      /**  NAFTA Preference Code  */  
   "NAFTAPref":string,
      /**  Export License Type  */  
   "ExpLicType":string,
      /**  Export License Number  */  
   "ExpLicNumber":string,
      /**  ECCN Number  */  
   "ECCNNumber":string,
      /**  AES Export code  */  
   "AESExp":string,
      /**  Harmonized Tariff Schedule Code  */  
   "HTS":string,
      /**  Use HTS description flag - for shippers shippers export declaration  */  
   "UseHTSDesc":boolean,
      /**  Schedule B Code  */  
   "SchedBcode":string,
      /**  Hazardous Item  */  
   "HazItem":boolean,
      /**  Hazardous Technical Name  */  
   "HazTechName":string,
      /**  Hazardous Class Number  */  
   "HazClass":string,
      /**  Hazardous Subrisk Class  */  
   "HazSub":string,
      /**  Hazardous Government Assigned ID  */  
   "HazGvrnmtID":string,
      /**  Hazardous Packing instructions  */  
   "HazPackInstr":string,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this Part.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the invoice line for this Part.  */  
   "RevChargeMethod":string,
      /**  Reverse Charge Under Threshold value. If the absolute value of an invoice line is less than the under threshold then the reverse charge tax code will be applied.  */  
   "RCUnderThreshold":number,
      /**  Reverse Charge Over Threshold value. If the absolute value of an invoice line is more than the over threshold then the reverse charge tax code will be applied.  */  
   "RCOverThreshold":number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**   The UOM Class that will be used for the Part. The UOM Class establishes the list of unit of measures that can be used in reference to this part.
Must be valid in the UOMClass table.  */  
   "UOMClassID":string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   "SNMaskSuffix":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   "SNMaskPrefix":string,
      /**  This is the last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It will be used when defaulting the SNLastUsedSeq field for new PartSite records.  */  
   "SNLastUsedSeq":string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   "UseMaskSeq":boolean,
      /**   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  */  
   "NetWeightUOM":string,
      /**   Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  */  
   "NetVolumeUOM":string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotBatch":boolean,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgBatch":boolean,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgLot":boolean,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotHeat":boolean,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotFirmware":boolean,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotBeforeDt":boolean,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotMfgDt":boolean,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotCureDt":boolean,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   "LotExpDt":boolean,
      /**  Defines a prefix to be used when a lot number is generated for the specific part.  */  
   "LotPrefix":string,
      /**  When generating the numeric portion of a lot number it can be either based on a next available number for the part (see Part.LotNextNum) or next available number from a Global Sequence (see LotSeq table and Part.LotSeqID)  */  
   "LotUseGlobalSeq":boolean,
      /**  The LotSeqID of the LotSeq record to use to retreive next available number when the part is using a Global Sequence  (Part.LotUseGlobalSeq = True). Must be valid in the LotSeq table if Part.LotUseGlobalSeq = True)  */  
   "LotSeqID":string,
      /**  The next available number to use to generate new lot numbers a part when the  is configured to use "Part Specific" number sequence. (Part.LotUseGlobalSeq = false).  */  
   "LotNxtNum":number,
      /**  Number of digits of the Next Avail Lot Number controls that will be used by system Generate lot number logic.  */  
   "LotDigits":number,
      /**  If leading zeros should be included in the numeric portion of the system generated lot number.  */  
   "LotLeadingZeros":boolean,
      /**   Option to append a trailing date string to the system generated lot number. The Date is the current system date.
Valid options are: None (Default), DD, MM, YYYY, MMYYYY, MM_YYYY, DDMMYYY, DD-MM-YYY, MMDDYYYY, MM-DD-YYYY,  YYYYMMDD, YYYY-MM-DD  */  
   "LotAppendDate":string,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   "BuyToOrder":boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   "DropShip":boolean,
      /**  Configured Part  */  
   "IsConfigured":boolean,
      /**  External Configurator  */  
   "ExtConfig":boolean,
      /**  The reference category that this Part belongs to.  */  
   "RefCategory":string,
      /**   Malaysia Localization
The flag to indicate that the part is under CJ5 jurisdiction  */  
   "CSFCJ5":boolean,
      /**   Malaysa Localization
The flag to indicate that the part is under LMW jurisdiction  */  
   "CSFLMW":boolean,
      /**  The Part's Unit Gross Weight.  */  
   "GrossWeight":number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  when creating new part records.  */  
   "GrossWeightUOM":string,
      /**  The part number used to identify the configured part number this part number was generated from.  */  
   "BasePartNum":string,
      /**  Class Code Entry Field  */  
   "FSAssetClassCode":string,
      /**  Field Service Sales Unit Price  */  
   "FSSalesUnitPrice":number,
      /**  Indicates the field service sales pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. The initial default is "E".  */  
   "FSPricePerCode":string,
      /**  Indicates if  Inspection is required upon receipt.  Inspection will also be enforced if the related Part Class, Vendor, PO Detail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  EstimateID  */  
   "EstimateID":string,
      /**  EstimateOrPlan  */  
   "EstimateOrPlan":string,
      /**  DiffPrc2PrchUOM  */  
   "DiffPrc2PrchUOM":boolean,
      /**  DupOnJobCrt  */  
   "DupOnJobCrt":boolean,
      /**  PricingFactor  */  
   "PricingFactor":number,
      /**  PricingUOM  */  
   "PricingUOM":string,
      /**  MobilePart  */  
   "MobilePart":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGUseGoodMark  */  
   "AGUseGoodMark":boolean,
      /**  AGProductMark  */  
   "AGProductMark":boolean,
      /**  ISRegion  */  
   "ISRegion":string,
      /**  INChapterID  */  
   "INChapterID":string,
      /**  CSF Peru -  SUNAT Type  */  
   "PESUNATType":string,
      /**  PESUNATUOM  */  
   "PESUNATUOM":string,
      /**  DEIsServices  */  
   "DEIsServices":boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   "DEIsSecurityFinancialDerivative":boolean,
      /**  DEInternationalSecuritiesID  */  
   "DEInternationalSecuritiesID":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  DEIsInvestment  */  
   "DEIsInvestment":boolean,
      /**  DEPayStatCode  */  
   "DEPayStatCode":string,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  PartLengthWidthHeightUM  */  
   "PartLengthWidthHeightUM":string,
      /**  DiameterUM  */  
   "DiameterUM":string,
      /**  DiameterInside  */  
   "DiameterInside":number,
      /**  DiameterOutside  */  
   "DiameterOutside":number,
      /**  ThicknessUM  */  
   "ThicknessUM":string,
      /**  Thickness  */  
   "Thickness":number,
      /**  ThicknessMax  */  
   "ThicknessMax":number,
      /**  Durometer  */  
   "Durometer":string,
      /**  Specification  */  
   "Specification":string,
      /**  EngineeringAlert  */  
   "EngineeringAlert":string,
      /**  Condition  */  
   "Condition":string,
      /**  IsCompliant  */  
   "IsCompliant":boolean,
      /**  IsRestricted  */  
   "IsRestricted":boolean,
      /**  IsSafetyItem  */  
   "IsSafetyItem":boolean,
      /**  CommercialBrand  */  
   "CommercialBrand":string,
      /**  CommercialSubBrand  */  
   "CommercialSubBrand":string,
      /**  CommercialCategory  */  
   "CommercialCategory":string,
      /**  CommercialSubCategory  */  
   "CommercialSubCategory":string,
      /**  CommercialStyle  */  
   "CommercialStyle":string,
      /**  CommercialSize1  */  
   "CommercialSize1":string,
      /**  CommercialSize2  */  
   "CommercialSize2":string,
      /**  CommercialColor  */  
   "CommercialColor":string,
      /**  IsGiftCard  */  
   "IsGiftCard":boolean,
      /**  PhotoFile  */  
   "PhotoFile":string,
      /**  PartPhotoExists  */  
   "PartPhotoExists":boolean,
      /**  CommentText  */  
   "CommentText":string,
      /**  Indicates if the packaging information is part specific or specified at the UOM class level.  */  
   "PartSpecificPackingUOM":boolean,
      /**  ImageID  */  
   "ImageID":string,
      /**  Specification Code for China GTI purposes  */  
   "CNSpecification":string,
      /**  This field defines if the part  is synchronized to an External CRM.  */  
   "SyncToExternalCRM":boolean,
      /**  This field holds the id of this part in the External CRM  */  
   "ExternalCRMPartID":string,
      /**  This field defines the last time that the  part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSync":string,
      /**  This fields determines if the part needs to be synchronized to the External CRM. If there are changes in the part master file , Epicor ERP automatically turns on this field.  */  
   "ExternalCRMSyncRequired":boolean,
      /**  PESUNATTypeCode  */  
   "PESUNATTypeCode":string,
      /**  PESUNATUOMCode  */  
   "PESUNATUOMCode":string,
      /**  Code Version for China GTI purposes  */  
   "CNCodeVersion":string,
      /**  Tax Category Code for China GTI purposes  */  
   "CNTaxCategoryCode":string,
      /**  Has Preferential Treatment value for China GTI purposes  */  
   "CNHasPreferentialTreatment":boolean,
      /**  Preferential Treatment Content for China GTI purposes  */  
   "CNPreferentialTreatmentContent":string,
      /**  Zero Tax Rate Mark for China GTI purposes  */  
   "CNZeroTaxRateMark":string,
      /**  SubLevelCode  */  
   "SubLevelCode":number,
      /**  Date the Part was created  */  
   "CreatedBy":string,
      /**  User the Part was created by  */  
   "CreatedOn":string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBatch":string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgBatch":string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgLot":string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttHeat":string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttFirmware":string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBeforeDt":string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgDt":string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttCureDt":string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttExpDt":string,
      /**  DeferManualEntry  */  
   "DeferManualEntry":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  */  
   "DeferPurchaseReceipt":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  */  
   "DeferJobReceipt":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  */  
   "DeferInspection":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  */  
   "DeferQtyAdjustment":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  */  
   "DeferInventoryMove":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  */  
   "DeferShipments":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  */  
   "DeferInventoryCounts":boolean,
      /**  DeferAssetDisposal  */  
   "DeferAssetDisposal":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  */  
   "DeferReturnMaterials":boolean,
      /**  MXProdServCode  */  
   "MXProdServCode":string,
      /**  Date/Time when the Part record was updated  */  
   "ChangedOn":string,
      /**  MXCustomsDuty  */  
   "MXCustomsDuty":string,
      /**  Determines if the Part has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  When the part is marked as Item, it will create an Item Resource in Epicor FSA.  */  
   "FSAItem":boolean,
      /**  When the part is marked as Equipment, it will create an Equipment Resource Template in Epicor FSA.  */  
   "FSAEquipment":boolean,
      /**  Bill of Lading Class. Additional data for the part required for LTL and International shipments.  */  
   "BOLClass":string,
      /**  Fair Market Value. Additional data for the part required for LTL and International shipments.  */  
   "FairMarketValue":number,
      /**  SAFTProdCategory  */  
   "SAFTProdCategory":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  Indicates if this part requires Identification Numbers shipment time.  This is disable if Track Location inventory is false.  */  
   "LocationIDNumReq":boolean,
      /**  Indicates if this part tracks Location Inventory.  */  
   "LocationTrackInv":boolean,
      /**  Set the default value of Location View for materials added in Engineering Workbench.  */  
   "LocationMtlView":boolean,
      /**  LCNRVReporting  */  
   "LCNRVReporting":boolean,
      /**  LCNRVEstimatedUnitPrice  */  
   "LCNRVEstimatedUnitPrice":number,
      /**  MXCustomsUMFrom  */  
   "MXCustomsUMFrom":string,
      /**  Default format ID used when assigning ID Numbers.  */  
   "LocationFormatID":string,
      /**  IsServices  */  
   "IsServices":boolean,
      /**  PEDetrGoodServiceCode  */  
   "PEDetrGoodServiceCode":string,
      /**  PEProductServiceCode  */  
   "PEProductServiceCode":string,
      /**  Dual UOM Class ID  */  
   "DualUOMClassID":string,
      /**  Product Name  */  
   "CNProductName":string,
      /**  Weight  */  
   "CNWeight":number,
      /**  Unit of Weight  */  
   "CNWeightUOM":string,
      /**  Bonded  */  
   "CNBonded":boolean,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "TrackInventoryAttributes":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "DefaultAttributeSetID":number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttISOrigCountry":string,
      /**  ISO / IEC 6523  */  
   "ExternalSchemeID":string,
      /**  Part ID  */  
   "ExternalID":string,
      /**  UNTDID 7143  */  
   "CommoditySchemeID":string,
      /**  Part Commodity Scheme Version  */  
   "CommoditySchemeVersion":string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
      /**  Indicates if this part performs MRP by Revision.  Requires Planning by Revision license.  */  
   "PlanningByRevision":boolean,
      /**  RcvInspectionReqPart  */  
   "RcvInspectionReqPart":string,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMPartType  */  
   "FSMPartType":number,
   "CountryNumDescription":string,
      /**  Should the Express Part Check Out option be enabled?  */  
   "EnableExpressCheckOut":boolean,
   "EnableGlobalLock":boolean,
   "EnableGlobalPart":boolean,
      /**  Indicates if the InActive flag should be available for input,  */  
   "EnableInActive":boolean,
      /**  Flag to tell UI whether the Part.IUM field should be enabled or not.  */  
   "EnableIUM":boolean,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   "EnableRevCharge":boolean,
      /**  Indicates if the Serial Number button should be enabled.  */  
   "EnableSerialNum":boolean,
      /**  This field is used only as a flag to determine in UI, if the Part.TrackSerialNum can be change.  */  
   "EnableTrackSerialNum":boolean,
      /**  Flag to tell UI whether the UOMClassID field should be enabled or not.  */  
   "EnableUOMClass":boolean,
   "ExtCoExist":boolean,
      /**  Default installation price of an equipment that requires installation in Epicor FSA.  */  
   "FSAInstallationCost":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   "FSAInstallationType":string,
   "FSAInstTypeDesc":string,
      /**  Indicates if the Part is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbPartNum that is linking to this part  */  
   "GlbLink":string,
      /**  check if TrackDimension is in GlbTable and should be disabled in Part Entry  */  
   "GlbTableAllowUpdTrackDim":boolean,
      /**  check if TrackLots is in GlbTable and should be disabled in Part Entry  */  
   "GlbTableAllowUpdTrackLots":boolean,
      /**  check if TrackSerialNum is in GlbTable and should be disabled in Part Entry  */  
   "GlbTableAllowUpdTrackSerial":boolean,
      /**  Indicates if there is any quantity on hand for this part  */  
   "HasOnHandQty":boolean,
      /**  Indicates if part is a component (has a where used list available)  */  
   "IsComponent":boolean,
      /**   This field indicates if the part is being used as a co-part anywhere.  This field will be used to prevent a Part from being marked as serial tracked or configured after being added as a co-part.

CoParts Project.  */  
   "IsCoPart":boolean,
      /**  This is the numeric value of ISOrigCountry.  */  
   "ISOrigCountryNum":number,
      /**  Shows what the next generated lot number for this part would look like  */  
   "NextGeneratedLotNum":string,
   "PEDetrGoodServiceCodeDesc":string,
   "PEProductServiceCodeDesc":string,
   "PLM":boolean,
      /**  Indicates if the PLM toggle box is enabled.  */  
   "PLMEnabled":boolean,
      /**  Revision  */  
   "Revision":boolean,
   "SalesUMDisp":string,
   "SNLeadingZeros":boolean,
   "SNMaskPrefixLength":number,
   "SNMaskSuffixLength":number,
   "SNNumODigits":number,
      /**  Yes means to copy the NonStock and CostMethod from Part to all the PartPlant records.  */  
   "UpdatePartPlant":boolean,
      /**  Indicates whether to update the Part serial number format changes to part plant  */  
   "UpdateSNPartPlant":boolean,
      /**  List of fields which are referenced by COA segments.  */  
   "COASegReferences":string,
      /**  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  */  
   "HasMRPPlanningAttribute":boolean,
   "UpdatePartPlantOverride":boolean,
      /**  DEPayStatCode Description  */  
   "DEPayStatCodeDescr":string,
      /**  DEDenomination Description  */  
   "DEDenominationDescr":string,
   "DefaultBuyerName":string,
   "DefaultPlannerName":string,
      /**  This field is used only as a flag to determine in UI, if the Part.TrackInventoryByRevision can be changed.  */  
   "EnableTrackByRevision":boolean,
      /**  indicated if this part has been linked to a global part  */  
   "LinkedToGlbPart":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "ClassDescription":string,
   "CommodityCodeSuppUnitsUOM":string,
   "CommodityCodeDescription":string,
   "CompanySendToFSA":boolean,
   "DualUOMClassIDDescription":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "FSAssetClassCodeFSAssetClassDesc":string,
   "Mtl_AnalysisCdDescription":string,
   "MXProdServCodeDesc":string,
   "OnHoldReasonCodeDescription":string,
   "ProdCodeDescription":string,
   "RefCategoryDescription":string,
   "SerialMaskMaskType":number,
   "SerialMaskDescription":string,
   "TaxCatIDDescription":string,
   "UOMClassIDDescription":string,
   "WarrantyCodeWarrDescription":string,
   "XbSystELIEinvoice":boolean,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "SalesCatID_c":string,
   "CustomBuyout_c":boolean,
   "NonSellable_c":boolean,
   "WebSearchable_c":boolean,
}

export interface Erp_Tablesets_QuoteDtlPARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   "Ordered":boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   "XPartNum":string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   "LeadTime":string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   "JobComment":string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   "MfgDetail":boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   "CustNum":number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Quoted":boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Expired":boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   "SellingExpectedQty":number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SellingExpectedUM":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   "ConfidencePct":number,
      /**  The date this line was last updated  */  
   "LastUpdate":string,
      /**  The last User Is that updated this Quote  */  
   "LastDcdUserID":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   "DocDiscount":number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "ExpectedRevenue":number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "DocExpectedRevenue":number,
      /**  The requested ship date for the sales order  */  
   "ReqShipDate":string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   "OrderQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingExpFactor":number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   "MultiRel":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   "SalesCatID":string,
      /**  Replicated from QuoteHed to easier sorting  */  
   "TerritoryID":string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   "CreatedFrom":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This is the unit price based on the expected quantity.  */  
   "ExpUnitPrice":number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   "DocExpUnitPrice":number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   "ExpPricePerCode":string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   "MiscQtyNum":number,
      /**  The Quote Line has been Engineered.  */  
   "Engineer":boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   "ReadyToQuote":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "QuoteHedDateQuoted":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "BitFlag":number,
   "CustNumCustIDBTName":string,
   "CustNumCustIDName":string,
   "CustNumCustIDCustID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface AfterGetRows_output{
}

export interface AllowProfitability_output{
}

export interface Erp_Tablesets_InvcDtlPARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Sales representative commission rate.  */  
   RepRate:number,
   RepSplit:number,
   InvcHeadInvoiceDate:string,
   InvcHeadCurrencyCode:string,
   InvcHeadCustID:string,
   InvcHeadCustName:string,
   TotalCost:number,
   ProfitLoss:number,
   ProfitLossPct:number,
   CustomerCustID:string,
   CustomerName:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadPARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff2:boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff3:boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff4:boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff5:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   SchedStatus:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The date that APS updated this record.  If this field is set then APS has scheduled the Job.  */  
   APSUpdatedDate:string,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  The time, in decimal hours, that APS updated the dates and times for this job.  This field is only valid if the APSUpdateDate field is set.  */  
   APSUpdatedTime:number,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Indicates that the quantity on this job is locked  */  
   LockQty:boolean,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   ProcessMode:string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   PlannedActionDate:string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   PlannedKitDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   EstTotalCost:number,
   ActualTotalCost:number,
   TotalVariance:number,
   EstLabor:number,
   EstBurden:number,
   EstMaterial:number,
   EstMtlBurden:number,
   EstSubcontract:number,
   ActLabor:number,
   ActBurden:number,
   ActMaterial:number,
   ActMtlBurden:number,
   ActSubcontract:number,
   VarLabor:number,
   VarBurden:number,
   VarMaterial:number,
   VarMtlBurden:number,
   VarSubcontract:number,
   EstSetupHrs:number,
   ActSetupHrs:number,
   EstProdHrs:number,
   ActProdHrs:number,
   EstTotalHrs:number,
   ActTotalHrs:number,
   VarTotalHrs:number,
   JobAsmblAssemblySeq:number,
   JobAsmblEstUnitCost:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderDtlPARow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OrderHedOrderDate:string,
   OrderHedPONum:string,
   CustomerCustID:string,
   CustomerCustName:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Phase_c:string,
   ItemID_c:string,
   TypeCode_c:string,
   OrigTypeCode_c:string,
   PhaseID_c:string,
   SalesCatID_c:string,
   IndustryShipDate_c:string,
   CreateDate_c:string,
   PriceUpdateDate_c:string,
   CreatedBy_c:string,
   UpdatedBy_c:string,
}

export interface Erp_Tablesets_PartAdvisorListTableset{
   PartList:Erp_Tablesets_PartListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAdvisorTableset{
   Part:Erp_Tablesets_PartRow[],
   PartAttch:Erp_Tablesets_PartAttchRow[],
   InvcDtlPA:Erp_Tablesets_InvcDtlPARow[],
   JobHeadPA:Erp_Tablesets_JobHeadPARow[],
   OrderDtlPA:Erp_Tablesets_OrderDtlPARow[],
   PartBin:Erp_Tablesets_PartBinRow[],
   QuoteDtlPA:Erp_Tablesets_QuoteDtlPARow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAttchRow{
   Company:string,
   PartNum:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartBinRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the Part Number. It must be valid in the Part table.  */  
   PartNum:string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**   Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.
Note: With 9.0 the OnHandQty value is in terms of unit of measure (PartBin.DimCode) and does not require any conversion displaying in that uom.  */  
   OnhandQty:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   DimCode:string,
      /**  A summary of the outstanding quantities for order open sales releases that are being filled from stock and of the open job material requirements that are to be issued from stock (JobMtl.Buyit = No) for this Part within a specific bin within the warehouse.  NOTE: This value is the TOTAL of job allocation PartAlloc.  */  
   AllocatedQty:number,
      /**  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled by stock in this bin in this warehouse and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  */  
   SalesAllocatedQty:number,
      /**   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickingQty:number,
      /**  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  */  
   SalesPickedQty:number,
      /**  New in 9.00.  Summary of mfg demands on firm jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobHead.Released = No.  */  
   JobAllocatedQty:number,
      /**  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  */  
   JobPickingQty:number,
      /**  Stock Quantity picked for jobs.  */  
   JobPickedQty:number,
      /**  Summary of Transfer Order Allocated Qty for this Part in this Bin in this Warehouse.  */  
   TFOrdAllocatedQty:number,
      /**  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  */  
   TFOrdPickingQty:number,
      /**  Stock Quantity picked for transfer orders.  */  
   TFOrdPickedQty:number,
      /**  Holds the Quantity in the Shipping process in the warehouse from this specific bin location.  */  
   ShippingQty:number,
      /**  Amount in Bin that is in a Packaging Unit.  */  
   PackedQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  Determines if the PartBin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  */  
   CountedDate:string,
      /**  When tracking inventory attributes this is the quantity per piece in the inventory UOM used to calculate Nbr. Of Pieces.  */  
   QtyPerPiece:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   BinNumDescription:string,
   DimCodeDimCodeDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   ClassID:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   PUM:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   TrackDimension:boolean,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  */  
   QtyBearing:boolean,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotBatch:boolean,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgBatch:boolean,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgLot:boolean,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotHeat:boolean,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotFirmware:boolean,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotBeforeDt:boolean,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgDt:boolean,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotCureDt:boolean,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotExpDt:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBatch:string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgBatch:string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgLot:string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttHeat:string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttFirmware:string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBeforeDt:string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgDt:string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttCureDt:string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttExpDt:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   DefaultAttributeSetID:number,
      /**  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  */  
   HasMRPPlanningAttribute:boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   ClassID:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   PUM:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.


Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   PurchasingFactor:number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PricePerCode:string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   InternalUnitPrice:number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   InternalPricePerCode:string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   MfgComment:string,
      /**   Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   PurComment:string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   CostMethod:string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar1Label
is non blank.  */  
   UserChar1:string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar2Label
is non blank.  */  
   UserChar2:string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar3Label
is non blank.  */  
   UserChar3:string,
      /**   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar4Label
is non blank.  */  
   UserChar4:string,
      /**   User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate1Label
is non blank.  */  
   UserDate1:string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate2Label is non blank.  */  
   UserDate2:string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate3 Label is non blank.  */  
   UserDate3:string,
      /**  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate4 Label is non blank.  */  
   UserDate4:string,
      /**   User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec1Label
is non blank.  */  
   UserDecimal1:number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec2Label is non blank.  */  
   UserDecimal2:number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec3Label is non blank.  */  
   UserDecimal3:number,
      /**  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec4Label is non blank.  */  
   UserDecimal4:number,
      /**  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt1Label is non blank.  */  
   UserInteger1:number,
      /**  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt2Label is non blank.  */  
   UserInteger2:number,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   LowLevelCode:number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   TrackDimension:boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DefaultDim:string,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Unique code for the Warranty for this part  */  
   WarrantyCode:string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**  The Part's Unit Net Weight.  */  
   NetWeight:number,
      /**  if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   UsePartRev:boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   PartsPerContainer:number,
      /**  Part's length.  */  
   PartLength:number,
      /**  Part's width.  */  
   PartWidth:number,
      /**  Part's Height.  */  
   PartHeight:number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   LotShelfLife:number,
      /**  This is a Web saleable part  */  
   WebPart:boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   RunOut:boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   SubPart:string,
      /**  Part's diameter.  */  
   Diameter:number,
      /**  Part's gravity.  */  
   Gravity:number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   OnHoldDate:string,
      /**  The Reason.Code associate with the reason why the part has been placed on hold. Valid only when Part.OnHold = Yes.  */  
   OnHoldReasonCode:string,
      /**  Default analysis code to be used when this part appears as an assembly  on a quote or a job.  */  
   AnalysisCode:string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   GlobalPart:boolean,
      /**  MtlAnalysisCode  */  
   MtlAnalysisCode:string,
      /**  Disables this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   ISSuppUnitsFactor:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   ImageFileName:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
      /**  Current setting for the prefix that will be attached to all new Serial Numbers as they are generated.  */  
   SNPrefix:string,
      /**  Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999  */  
   SNFormat:string,
      /**  Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer  */  
   SNBaseDataType:string,
      /**  Used by the scheduling process when a part is stocked.  When TRUE,  the availability of this Part must be calculated via the TimePhase process prior to scheduling a Job.  */  
   Constrained:boolean,
      /**  UPS / UCC Code required by some industries.  */  
   UPCCode1:string,
      /**  UPS / UCC Code required by some industries.  */  
   UPCCode2:string,
      /**  UPS / UCC Code required by some industries.  */  
   UPCCode3:string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  For Customer Connect Only.  This field is used in Store Front to indicate if the part is available in stock.  */  
   WebInStock:boolean,
      /**  Should this Part be included in Consolidated Purchasing?  */  
   ConsolidatedPurchasing:boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**   Receiving Documents Required.
Indicates receiving documents are required when receiving this part.  This pertains only to lot tracked parts that are received to inventory. If checked, then at the time of receiving the system will require that one or more attachments with a reference to a DocType having Receipt = yes be entered.Requires DocManagement license.  */  
   RecDocReq:boolean,
      /**  Maximum daily production value.  Used in demand shipping schedule.  */  
   MDPV:number,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part. Pertains to Inventory shipments of lot tracked parts or shipments directly from the job only. If checked, then at the time of shipping the system will require that the PartLot.Ship DocsAvail, or JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   ShipDocReq:boolean,
      /**  The returnable container for this part when the part needs to be returned.  The value is provided by the trading partner.  */  
   ReturnableContainer:string,
      /**  The Part's Net Volume.  */  
   NetVolume:number,
      /**  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  */  
   QtyBearing:boolean,
      /**  This field contains the Country of Origin Code from the Country table.  For International shipping.  */  
   NAFTAOrigCountry:string,
      /**  NAFTA Producer Code - For international shipping  */  
   NAFTAProd:string,
      /**  NAFTA Preference Code  */  
   NAFTAPref:string,
      /**  Export License Type  */  
   ExpLicType:string,
      /**  Export License Number  */  
   ExpLicNumber:string,
      /**  ECCN Number  */  
   ECCNNumber:string,
      /**  AES Export code  */  
   AESExp:string,
      /**  Harmonized Tariff Schedule Code  */  
   HTS:string,
      /**  Use HTS description flag - for shippers shippers export declaration  */  
   UseHTSDesc:boolean,
      /**  Schedule B Code  */  
   SchedBcode:string,
      /**  Hazardous Item  */  
   HazItem:boolean,
      /**  Hazardous Technical Name  */  
   HazTechName:string,
      /**  Hazardous Class Number  */  
   HazClass:string,
      /**  Hazardous Subrisk Class  */  
   HazSub:string,
      /**  Hazardous Government Assigned ID  */  
   HazGvrnmtID:string,
      /**  Hazardous Packing instructions  */  
   HazPackInstr:string,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this Part.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the invoice line for this Part.  */  
   RevChargeMethod:string,
      /**  Reverse Charge Under Threshold value. If the absolute value of an invoice line is less than the under threshold then the reverse charge tax code will be applied.  */  
   RCUnderThreshold:number,
      /**  Reverse Charge Over Threshold value. If the absolute value of an invoice line is more than the over threshold then the reverse charge tax code will be applied.  */  
   RCOverThreshold:number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**   The UOM Class that will be used for the Part. The UOM Class establishes the list of unit of measures that can be used in reference to this part.
Must be valid in the UOMClass table.  */  
   UOMClassID:string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It will be used when defaulting the SNLastUsedSeq field for new PartSite records.  */  
   SNLastUsedSeq:string,
      /**  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  */  
   UseMaskSeq:boolean,
      /**   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  */  
   NetWeightUOM:string,
      /**   Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  */  
   NetVolumeUOM:string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotBatch:boolean,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgBatch:boolean,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgLot:boolean,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotHeat:boolean,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotFirmware:boolean,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotBeforeDt:boolean,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotMfgDt:boolean,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotCureDt:boolean,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  */  
   LotExpDt:boolean,
      /**  Defines a prefix to be used when a lot number is generated for the specific part.  */  
   LotPrefix:string,
      /**  When generating the numeric portion of a lot number it can be either based on a next available number for the part (see Part.LotNextNum) or next available number from a Global Sequence (see LotSeq table and Part.LotSeqID)  */  
   LotUseGlobalSeq:boolean,
      /**  The LotSeqID of the LotSeq record to use to retreive next available number when the part is using a Global Sequence  (Part.LotUseGlobalSeq = True). Must be valid in the LotSeq table if Part.LotUseGlobalSeq = True)  */  
   LotSeqID:string,
      /**  The next available number to use to generate new lot numbers a part when the  is configured to use "Part Specific" number sequence. (Part.LotUseGlobalSeq = false).  */  
   LotNxtNum:number,
      /**  Number of digits of the Next Avail Lot Number controls that will be used by system Generate lot number logic.  */  
   LotDigits:number,
      /**  If leading zeros should be included in the numeric portion of the system generated lot number.  */  
   LotLeadingZeros:boolean,
      /**   Option to append a trailing date string to the system generated lot number. The Date is the current system date.
Valid options are: None (Default), DD, MM, YYYY, MMYYYY, MM_YYYY, DDMMYYY, DD-MM-YYY, MMDDYYYY, MM-DD-YYYY,  YYYYMMDD, YYYY-MM-DD  */  
   LotAppendDate:string,
      /**  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  */  
   BuyToOrder:boolean,
      /**  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  */  
   DropShip:boolean,
      /**  Configured Part  */  
   IsConfigured:boolean,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  The reference category that this Part belongs to.  */  
   RefCategory:string,
      /**   Malaysia Localization
The flag to indicate that the part is under CJ5 jurisdiction  */  
   CSFCJ5:boolean,
      /**   Malaysa Localization
The flag to indicate that the part is under LMW jurisdiction  */  
   CSFLMW:boolean,
      /**  The Part's Unit Gross Weight.  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  when creating new part records.  */  
   GrossWeightUOM:string,
      /**  The part number used to identify the configured part number this part number was generated from.  */  
   BasePartNum:string,
      /**  Class Code Entry Field  */  
   FSAssetClassCode:string,
      /**  Field Service Sales Unit Price  */  
   FSSalesUnitPrice:number,
      /**  Indicates the field service sales pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. The initial default is "E".  */  
   FSPricePerCode:string,
      /**  Indicates if  Inspection is required upon receipt.  Inspection will also be enforced if the related Part Class, Vendor, PO Detail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  EstimateID  */  
   EstimateID:string,
      /**  EstimateOrPlan  */  
   EstimateOrPlan:string,
      /**  DiffPrc2PrchUOM  */  
   DiffPrc2PrchUOM:boolean,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  PricingFactor  */  
   PricingFactor:number,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  MobilePart  */  
   MobilePart:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGUseGoodMark  */  
   AGUseGoodMark:boolean,
      /**  AGProductMark  */  
   AGProductMark:boolean,
      /**  ISRegion  */  
   ISRegion:string,
      /**  INChapterID  */  
   INChapterID:string,
      /**  CSF Peru -  SUNAT Type  */  
   PESUNATType:string,
      /**  PESUNATUOM  */  
   PESUNATUOM:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  PartLengthWidthHeightUM  */  
   PartLengthWidthHeightUM:string,
      /**  DiameterUM  */  
   DiameterUM:string,
      /**  DiameterInside  */  
   DiameterInside:number,
      /**  DiameterOutside  */  
   DiameterOutside:number,
      /**  ThicknessUM  */  
   ThicknessUM:string,
      /**  Thickness  */  
   Thickness:number,
      /**  ThicknessMax  */  
   ThicknessMax:number,
      /**  Durometer  */  
   Durometer:string,
      /**  Specification  */  
   Specification:string,
      /**  EngineeringAlert  */  
   EngineeringAlert:string,
      /**  Condition  */  
   Condition:string,
      /**  IsCompliant  */  
   IsCompliant:boolean,
      /**  IsRestricted  */  
   IsRestricted:boolean,
      /**  IsSafetyItem  */  
   IsSafetyItem:boolean,
      /**  CommercialBrand  */  
   CommercialBrand:string,
      /**  CommercialSubBrand  */  
   CommercialSubBrand:string,
      /**  CommercialCategory  */  
   CommercialCategory:string,
      /**  CommercialSubCategory  */  
   CommercialSubCategory:string,
      /**  CommercialStyle  */  
   CommercialStyle:string,
      /**  CommercialSize1  */  
   CommercialSize1:string,
      /**  CommercialSize2  */  
   CommercialSize2:string,
      /**  CommercialColor  */  
   CommercialColor:string,
      /**  IsGiftCard  */  
   IsGiftCard:boolean,
      /**  PhotoFile  */  
   PhotoFile:string,
      /**  PartPhotoExists  */  
   PartPhotoExists:boolean,
      /**  CommentText  */  
   CommentText:string,
      /**  Indicates if the packaging information is part specific or specified at the UOM class level.  */  
   PartSpecificPackingUOM:boolean,
      /**  ImageID  */  
   ImageID:string,
      /**  Specification Code for China GTI purposes  */  
   CNSpecification:string,
      /**  This field defines if the part  is synchronized to an External CRM.  */  
   SyncToExternalCRM:boolean,
      /**  This field holds the id of this part in the External CRM  */  
   ExternalCRMPartID:string,
      /**  This field defines the last time that the  part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSync:string,
      /**  This fields determines if the part needs to be synchronized to the External CRM. If there are changes in the part master file , Epicor ERP automatically turns on this field.  */  
   ExternalCRMSyncRequired:boolean,
      /**  PESUNATTypeCode  */  
   PESUNATTypeCode:string,
      /**  PESUNATUOMCode  */  
   PESUNATUOMCode:string,
      /**  Code Version for China GTI purposes  */  
   CNCodeVersion:string,
      /**  Tax Category Code for China GTI purposes  */  
   CNTaxCategoryCode:string,
      /**  Has Preferential Treatment value for China GTI purposes  */  
   CNHasPreferentialTreatment:boolean,
      /**  Preferential Treatment Content for China GTI purposes  */  
   CNPreferentialTreatmentContent:string,
      /**  Zero Tax Rate Mark for China GTI purposes  */  
   CNZeroTaxRateMark:string,
      /**  SubLevelCode  */  
   SubLevelCode:number,
      /**  Date the Part was created  */  
   CreatedBy:string,
      /**  User the Part was created by  */  
   CreatedOn:string,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBatch:string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgBatch:string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgLot:string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttHeat:string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttFirmware:string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBeforeDt:string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgDt:string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttCureDt:string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttExpDt:string,
      /**  DeferManualEntry  */  
   DeferManualEntry:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  */  
   DeferPurchaseReceipt:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  */  
   DeferJobReceipt:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  */  
   DeferInspection:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  */  
   DeferQtyAdjustment:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  */  
   DeferInventoryMove:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  */  
   DeferShipments:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  */  
   DeferInventoryCounts:boolean,
      /**  DeferAssetDisposal  */  
   DeferAssetDisposal:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  */  
   DeferReturnMaterials:boolean,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Date/Time when the Part record was updated  */  
   ChangedOn:string,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  Determines if the Part has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  When the part is marked as Item, it will create an Item Resource in Epicor FSA.  */  
   FSAItem:boolean,
      /**  When the part is marked as Equipment, it will create an Equipment Resource Template in Epicor FSA.  */  
   FSAEquipment:boolean,
      /**  Bill of Lading Class. Additional data for the part required for LTL and International shipments.  */  
   BOLClass:string,
      /**  Fair Market Value. Additional data for the part required for LTL and International shipments.  */  
   FairMarketValue:number,
      /**  SAFTProdCategory  */  
   SAFTProdCategory:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Indicates if this part requires Identification Numbers shipment time.  This is disable if Track Location inventory is false.  */  
   LocationIDNumReq:boolean,
      /**  Indicates if this part tracks Location Inventory.  */  
   LocationTrackInv:boolean,
      /**  Set the default value of Location View for materials added in Engineering Workbench.  */  
   LocationMtlView:boolean,
      /**  LCNRVReporting  */  
   LCNRVReporting:boolean,
      /**  LCNRVEstimatedUnitPrice  */  
   LCNRVEstimatedUnitPrice:number,
      /**  MXCustomsUMFrom  */  
   MXCustomsUMFrom:string,
      /**  Default format ID used when assigning ID Numbers.  */  
   LocationFormatID:string,
      /**  IsServices  */  
   IsServices:boolean,
      /**  PEDetrGoodServiceCode  */  
   PEDetrGoodServiceCode:string,
      /**  PEProductServiceCode  */  
   PEProductServiceCode:string,
      /**  Dual UOM Class ID  */  
   DualUOMClassID:string,
      /**  Product Name  */  
   CNProductName:string,
      /**  Weight  */  
   CNWeight:number,
      /**  Unit of Weight  */  
   CNWeightUOM:string,
      /**  Bonded  */  
   CNBonded:boolean,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   DefaultAttributeSetID:number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttISOrigCountry:string,
      /**  ISO / IEC 6523  */  
   ExternalSchemeID:string,
      /**  Part ID  */  
   ExternalID:string,
      /**  UNTDID 7143  */  
   CommoditySchemeID:string,
      /**  Part Commodity Scheme Version  */  
   CommoditySchemeVersion:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
      /**  Indicates if this part performs MRP by Revision.  Requires Planning by Revision license.  */  
   PlanningByRevision:boolean,
      /**  RcvInspectionReqPart  */  
   RcvInspectionReqPart:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMPartType  */  
   FSMPartType:number,
   CountryNumDescription:string,
      /**  Should the Express Part Check Out option be enabled?  */  
   EnableExpressCheckOut:boolean,
   EnableGlobalLock:boolean,
   EnableGlobalPart:boolean,
      /**  Indicates if the InActive flag should be available for input,  */  
   EnableInActive:boolean,
      /**  Flag to tell UI whether the Part.IUM field should be enabled or not.  */  
   EnableIUM:boolean,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   EnableRevCharge:boolean,
      /**  Indicates if the Serial Number button should be enabled.  */  
   EnableSerialNum:boolean,
      /**  This field is used only as a flag to determine in UI, if the Part.TrackSerialNum can be change.  */  
   EnableTrackSerialNum:boolean,
      /**  Flag to tell UI whether the UOMClassID field should be enabled or not.  */  
   EnableUOMClass:boolean,
   ExtCoExist:boolean,
      /**  Default installation price of an equipment that requires installation in Epicor FSA.  */  
   FSAInstallationCost:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   FSAInstallationType:string,
   FSAInstTypeDesc:string,
      /**  Indicates if the Part is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbPartNum that is linking to this part  */  
   GlbLink:string,
      /**  check if TrackDimension is in GlbTable and should be disabled in Part Entry  */  
   GlbTableAllowUpdTrackDim:boolean,
      /**  check if TrackLots is in GlbTable and should be disabled in Part Entry  */  
   GlbTableAllowUpdTrackLots:boolean,
      /**  check if TrackSerialNum is in GlbTable and should be disabled in Part Entry  */  
   GlbTableAllowUpdTrackSerial:boolean,
      /**  Indicates if there is any quantity on hand for this part  */  
   HasOnHandQty:boolean,
      /**  Indicates if part is a component (has a where used list available)  */  
   IsComponent:boolean,
      /**   This field indicates if the part is being used as a co-part anywhere.  This field will be used to prevent a Part from being marked as serial tracked or configured after being added as a co-part.

CoParts Project.  */  
   IsCoPart:boolean,
      /**  This is the numeric value of ISOrigCountry.  */  
   ISOrigCountryNum:number,
      /**  Shows what the next generated lot number for this part would look like  */  
   NextGeneratedLotNum:string,
   PEDetrGoodServiceCodeDesc:string,
   PEProductServiceCodeDesc:string,
   PLM:boolean,
      /**  Indicates if the PLM toggle box is enabled.  */  
   PLMEnabled:boolean,
      /**  Revision  */  
   Revision:boolean,
   SalesUMDisp:string,
   SNLeadingZeros:boolean,
   SNMaskPrefixLength:number,
   SNMaskSuffixLength:number,
   SNNumODigits:number,
      /**  Yes means to copy the NonStock and CostMethod from Part to all the PartPlant records.  */  
   UpdatePartPlant:boolean,
      /**  Indicates whether to update the Part serial number format changes to part plant  */  
   UpdateSNPartPlant:boolean,
      /**  List of fields which are referenced by COA segments.  */  
   COASegReferences:string,
      /**  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  */  
   HasMRPPlanningAttribute:boolean,
   UpdatePartPlantOverride:boolean,
      /**  DEPayStatCode Description  */  
   DEPayStatCodeDescr:string,
      /**  DEDenomination Description  */  
   DEDenominationDescr:string,
   DefaultBuyerName:string,
   DefaultPlannerName:string,
      /**  This field is used only as a flag to determine in UI, if the Part.TrackInventoryByRevision can be changed.  */  
   EnableTrackByRevision:boolean,
      /**  indicated if this part has been linked to a global part  */  
   LinkedToGlbPart:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   ClassDescription:string,
   CommodityCodeSuppUnitsUOM:string,
   CommodityCodeDescription:string,
   CompanySendToFSA:boolean,
   DualUOMClassIDDescription:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   FSAssetClassCodeFSAssetClassDesc:string,
   Mtl_AnalysisCdDescription:string,
   MXProdServCodeDesc:string,
   OnHoldReasonCodeDescription:string,
   ProdCodeDescription:string,
   RefCategoryDescription:string,
   SerialMaskMaskType:number,
   SerialMaskDescription:string,
   TaxCatIDDescription:string,
   UOMClassIDDescription:string,
   WarrantyCodeWarrDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   SalesCatID_c:string,
   CustomBuyout_c:boolean,
   NonSellable_c:boolean,
   WebSearchable_c:boolean,
}

export interface Erp_Tablesets_QuoteDtlPARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   XPartNum:string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   LeadTime:string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   JobComment:string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   MfgDetail:boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Quoted:boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Expired:boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SellingExpectedUM:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   ConfidencePct:number,
      /**  The date this line was last updated  */  
   LastUpdate:string,
      /**  The last User Is that updated this Quote  */  
   LastDcdUserID:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   DocDiscount:number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  The requested ship date for the sales order  */  
   ReqShipDate:string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   OrderQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingExpFactor:number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   MultiRel:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   SalesCatID:string,
      /**  Replicated from QuoteHed to easier sorting  */  
   TerritoryID:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   CreatedFrom:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This is the unit price based on the expected quantity.  */  
   ExpUnitPrice:number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   DocExpUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   ExpPricePerCode:string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   MiscQtyNum:number,
      /**  The Quote Line has been Engineered.  */  
   Engineer:boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   ReadyToQuote:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   QuoteHedDateQuoted:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   BitFlag:number,
   CustNumCustIDBTName:string,
   CustNumCustIDName:string,
   CustNumCustIDCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  Entered PartNum  */  
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
   */  
export interface GetByIDWithCounters_input{
      /**  Part Number  */  
   ipPartNum:string,
}

export interface GetByIDWithCounters_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   profitableCounter:number,
   producedCounter:number,
   soldCounter:number,
   quotedCounter:number,
   onHandExists:boolean,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface GetByID_input{
      /**  Part Number  */  
   ipPartNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param whereClauseInvcDtlPA
      @param pageSize
      @param absolutePage
   */  
export interface GetInvcDtlPAList_input{
      /**  The where clause to restrict data for  */  
   whereClauseInvcDtlPA:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetInvcDtlPAList_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetInvcDtlPARows_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetInvcDtlPARows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param whereClauseJobHeadPA
      @param pageSize
      @param absolutePage
   */  
export interface GetJobHeadPAList_input{
      /**  The where clause to restrict data for  */  
   whereClauseJobHeadPA:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetJobHeadPAList_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetJobHeadPARows_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetJobHeadPARows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  The criteria  */  
   whereClause:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PartAdvisorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderDtlPA
      @param pageSize
      @param absolutePage
   */  
export interface GetOrderDtlPAList_input{
      /**  The where clause to restrict data for  */  
   whereClauseOrderDtlPA:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetOrderDtlPAList_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetOrderDtlPARows_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetOrderDtlPARows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param whereClausePartBin
      @param pageSize
      @param absolutePage
   */  
export interface GetPartBinList_input{
      /**  The where clause to restrict data for  */  
   whereClausePartBin:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetPartBinList_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetPartBinRows_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetPartBinRows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param iPartNum
   */  
export interface GetPartDetails_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetPartDetails_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param whereClauseQuoteDtlPA
      @param pageSize
      @param absolutePage
   */  
export interface GetQuoteDtlPAList_input{
      /**  The where clause to restrict data for  */  
   whereClauseQuoteDtlPA:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetQuoteDtlPAList_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iPartNum
   */  
export interface GetQuoteDtlPARows_input{
      /**  Part Number for which you want details  */  
   iPartNum:string,
}

export interface GetQuoteDtlPARows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
}

   /** Required : 
      @param whereClausePart
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  The criteria  */  
   whereClausePart:string,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartAdvisorTableset[],
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

