import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLCostTransSvc
# Description: Cost transaction details for Chart Tracker.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLCostTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLCostTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLCostTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans",headers=creds) as resp:
           return await resp.json()

async def post_GLCostTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLCostTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLCostTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLCostTran item
   Description: Calls GetByID to retrieve the GLCostTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLCostTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLCostTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLCostTran for the service
   Description: Calls UpdateExt to update GLCostTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLCostTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLCostTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLCostTran item
   Description: Call UpdateExt to delete GLCostTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLCostTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/GLCostTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls",headers=creds) as resp:
           return await resp.json()

async def post_InvcDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcDtl item
   Description: Calls GetByID to retrieve the InvcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InvcDtl for the service
   Description: Calls UpdateExt to update InvcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InvcDtls_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InvcDtl item
   Description: Call UpdateExt to delete InvcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/InvcDtls(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtl item
   Description: Calls GetByID to retrieve the LaborDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtl for the service
   Description: Calls UpdateExt to update LaborDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtls_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtl item
   Description: Call UpdateExt to delete LaborDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/LaborDtls(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartTran, whereClauseInvcDtl, whereClauseLaborDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartTran=" + whereClausePartTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInvcDtl=" + whereClauseInvcDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtl=" + whereClauseLaborDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysDate, sysTime, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysDate=" + sysDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysTime=" + sysTime
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetRows method.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLCostTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranRow] = obj["value"]
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      """  Optional lot number description.  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumSP:str = obj["PartNumSP"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      """  First address line  """  
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      """  Second address line  """  
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      """  Third address line  """  
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      """  City portion of the address  """  
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      """  State portion of the address  """  
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.FromPlantName:str = obj["FromPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      """  Description.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.EnableSerialNumbers:bool = obj["EnableSerialNumbers"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumSP:str = obj["PartNumSP"]
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranAmount:int = obj["TranAmount"]
      """  Transaction Amount  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      self.RevisionNumMS:str = obj["RevisionNumMS"]
      self.RevisionNumSP:str = obj["RevisionNumSP"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AttributeSetDescriptionMS:str = obj["AttributeSetDescriptionMS"]
      """  Description for AttributeSetID associated with PartNumMS  """  
      self.AttributeSetIDMS:int = obj["AttributeSetIDMS"]
      """  AttributeSetID associated with PartNumMS  """  
      self.AttributeSetShortDescriptionMS:str = obj["AttributeSetShortDescriptionMS"]
      """  AttributeSetShortDescription associated with PartNumMS  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MatNumLineDesc:str = obj["MatNumLineDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLCostTransTableset:
   def __init__(self, obj):
      self.PartTran:list[Erp_Tablesets_PartTranRow] = obj["PartTran"]
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      """  Optional lot number description.  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumSP:str = obj["PartNumSP"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      """  First address line  """  
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      """  Second address line  """  
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      """  Third address line  """  
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      """  City portion of the address  """  
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      """  State portion of the address  """  
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.FromPlantName:str = obj["FromPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      """  Description.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranListTableset:
   def __init__(self, obj):
      self.PartTranList:list[Erp_Tablesets_PartTranListRow] = obj["PartTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.EnableSerialNumbers:bool = obj["EnableSerialNumbers"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumSP:str = obj["PartNumSP"]
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranAmount:int = obj["TranAmount"]
      """  Transaction Amount  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      self.RevisionNumMS:str = obj["RevisionNumMS"]
      self.RevisionNumSP:str = obj["RevisionNumSP"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AttributeSetDescriptionMS:str = obj["AttributeSetDescriptionMS"]
      """  Description for AttributeSetID associated with PartNumMS  """  
      self.AttributeSetIDMS:int = obj["AttributeSetIDMS"]
      """  AttributeSetID associated with PartNumMS  """  
      self.AttributeSetShortDescriptionMS:str = obj["AttributeSetShortDescriptionMS"]
      """  AttributeSetShortDescription associated with PartNumMS  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MatNumLineDesc:str = obj["MatNumLineDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGLCostTransTableset:
   def __init__(self, obj):
      self.PartTran:list[Erp_Tablesets_PartTranRow] = obj["PartTran"]
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCostTransTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCostTransTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCostTransTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcDtl_input:
   """ Required : 
   ds
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewInvcDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtl_input:
   """ Required : 
   ds
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetNewLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartTran_input:
   """ Required : 
   ds
   sysDate
   sysTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      pass

class GetNewPartTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   GLJrnDtlRowid
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.GLJrnDtlRowid:str = obj["GLJrnDtlRowid"]
      """  The GLJrnDtl Rowid  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCostTransTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartTran
   whereClauseInvcDtl
   whereClauseLaborDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartTran:str = obj["whereClausePartTran"]
      self.whereClauseInvcDtl:str = obj["whereClauseInvcDtl"]
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLCostTransTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLCostTransTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLCostTransTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLCostTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

