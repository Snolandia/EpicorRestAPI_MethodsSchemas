import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuoteAsmSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteAsms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsms
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms",headers=creds) as resp:
           return await resp.json()

async def post_QuoteAsms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsm item
   Description: Calls GetByID to retrieve the QuoteAsm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company, QuoteNum, QuoteLine, AssemblySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteAsm for the service
   Description: Calls UpdateExt to update QuoteAsm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq(Company, QuoteNum, QuoteLine, AssemblySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteAsm item
   Description: Call UpdateExt to delete QuoteAsm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmInsps(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteAsmInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmInsps",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmInsp item
   Description: Calls GetByID to retrieve the QuoteAsmInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteMtls(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteMtls",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtl item
   Description: Calls GetByID to retrieve the QuoteMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteOprs(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteOprs",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOpr item
   Description: Calls GetByID to retrieve the QuoteOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmRefDes(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteAsmRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmRefDes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmRefDes",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmRefDe item
   Description: Calls GetByID to retrieve the QuoteAsmRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmRefDe1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmAttches(Company, QuoteNum, QuoteLine, AssemblySeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteAsmAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteAsmAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmAttches",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsms_Company_QuoteNum_QuoteLine_AssemblySeq_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmAttch item
   Description: Calls GetByID to retrieve the QuoteAsmAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsms(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + ")/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteAsmInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps",headers=creds) as resp:
           return await resp.json()

async def post_QuoteAsmInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmInsp item
   Description: Calls GetByID to retrieve the QuoteAsmInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteAsmInsp for the service
   Description: Calls UpdateExt to update QuoteAsmInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteAsmInsps_Company_QuoteNum_QuoteLine_AssemblySeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteAsmInsp item
   Description: Call UpdateExt to delete QuoteAsmInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtls
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls",headers=creds) as resp:
           return await resp.json()

async def post_QuoteMtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtl item
   Description: Calls GetByID to retrieve the QuoteMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteMtl for the service
   Description: Calls UpdateExt to update QuoteMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteMtl item
   Description: Call UpdateExt to delete QuoteMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlInsps(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtlInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlInsps",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlInsp item
   Description: Calls GetByID to retrieve the QuoteMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlRefDes(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtlRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlRefDes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlRefDes",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlRefDe item
   Description: Calls GetByID to retrieve the QuoteMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlRefDe1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlAttches(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteMtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtls_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlAttch item
   Description: Calls GetByID to retrieve the QuoteMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + ")/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteMtlInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps",headers=creds) as resp:
           return await resp.json()

async def post_QuoteMtlInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlInsp item
   Description: Calls GetByID to retrieve the QuoteMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteMtlInsp for the service
   Description: Calls UpdateExt to update QuoteMtlInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteMtlInsps_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteMtlInsp item
   Description: Call UpdateExt to delete QuoteMtlInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlRefDes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteMtlRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlRefDes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes",headers=creds) as resp:
           return await resp.json()

async def post_QuoteMtlRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlRefDe item
   Description: Calls GetByID to retrieve the QuoteMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteMtlRefDe for the service
   Description: Calls UpdateExt to update QuoteMtlRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteMtlRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteMtlRefDe item
   Description: Call UpdateExt to delete QuoteMtlRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteMtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteMtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMtlAttch item
   Description: Calls GetByID to retrieve the QuoteMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteMtlAttch for the service
   Description: Calls UpdateExt to update QuoteMtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteMtlAttches_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteMtlAttch item
   Description: Call UpdateExt to delete QuoteMtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteMtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprs
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOpr item
   Description: Calls GetByID to retrieve the QuoteOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOpr for the service
   Description: Calls UpdateExt to update QuoteOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOpr item
   Description: Call UpdateExt to delete QuoteOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprActions(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprActions",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprAction item
   Description: Calls GetByID to retrieve the QuoteOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprInsps(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprInsps",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprInsp item
   Description: Calls GetByID to retrieve the QuoteOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOpDtls(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOpDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOpDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOpDtls",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOpDtl item
   Description: Calls GetByID to retrieve the QuoteOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprMachParams(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprMachParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprMachParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprMachParams",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, MachParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprMachParam item
   Description: Calls GetByID to retrieve the QuoteOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprMachParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprAttches(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprAttches",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprs_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprAttch item
   Description: Calls GetByID to retrieve the QuoteOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + ")/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprActions
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprAction item
   Description: Calls GetByID to retrieve the QuoteOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOprAction for the service
   Description: Calls UpdateExt to update QuoteOprAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOprAction item
   Description: Call UpdateExt to delete QuoteOprAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_QuoteOprActionParams(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteOprActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteOprActionParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")/QuoteOprActionParams",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActions_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprActionParam item
   Description: Calls GetByID to retrieve the QuoteOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprActionParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActions(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + ")/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActionParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprActionParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprActionParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprActionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprActionParam item
   Description: Calls GetByID to retrieve the QuoteOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, ActionParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOprActionParam for the service
   Description: Calls UpdateExt to update QuoteOprActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprActionParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_ActionSeq_ActionParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, ActionSeq, ActionParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOprActionParam item
   Description: Call UpdateExt to delete QuoteOprActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprActionParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprInsp item
   Description: Calls GetByID to retrieve the QuoteOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOprInsp for the service
   Description: Calls UpdateExt to update QuoteOprInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprInsps_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_PlanSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOprInsp item
   Description: Call UpdateExt to delete QuoteOprInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprInsps(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOpDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOpDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOpDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOpDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOpDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOpDtl item
   Description: Calls GetByID to retrieve the QuoteOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, OpDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOpDtl for the service
   Description: Calls UpdateExt to update QuoteOpDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOpDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOpDtls_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_OpDtlSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, OpDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOpDtl item
   Description: Call UpdateExt to delete QuoteOpDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOpDtls(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprMachParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprMachParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprMachParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprMachParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprMachParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, MachParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprMachParam item
   Description: Calls GetByID to retrieve the QuoteOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, MachParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOprMachParam for the service
   Description: Calls UpdateExt to update QuoteOprMachParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprMachParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprMachParams_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_MachParamSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, MachParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOprMachParam item
   Description: Call UpdateExt to delete QuoteOprMachParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprMachParams(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteOprAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteOprAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteOprAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteOprAttch item
   Description: Calls GetByID to retrieve the QuoteOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteOprAttch for the service
   Description: Calls UpdateExt to update QuoteOprAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteOprAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteOprAttches_Company_QuoteNum_QuoteLine_AssemblySeq_OprSeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, OprSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteOprAttch item
   Description: Call UpdateExt to delete QuoteOprAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteOprAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmRefDes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteAsmRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmRefDes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes",headers=creds) as resp:
           return await resp.json()

async def post_QuoteAsmRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmRefDe item
   Description: Calls GetByID to retrieve the QuoteAsmRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteAsmRefDe for the service
   Description: Calls UpdateExt to update QuoteAsmRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteAsmRefDes_Company_QuoteNum_QuoteLine_AssemblySeq_MtlSeq_RefDesSeq(Company, QuoteNum, QuoteLine, AssemblySeq, MtlSeq, RefDesSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteAsmRefDe item
   Description: Call UpdateExt to delete QuoteAsmRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmRefDes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteAsmAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteAsmAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteAsmAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteAsmAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteAsmAttch item
   Description: Calls GetByID to retrieve the QuoteAsmAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteAsmAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteAsmAttch for the service
   Description: Calls UpdateExt to update QuoteAsmAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteAsmAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteAsmAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteAsmAttches_Company_QuoteNum_QuoteLine_AssemblySeq_DrawingSeq(Company, QuoteNum, QuoteLine, AssemblySeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteAsmAttch item
   Description: Call UpdateExt to delete QuoteAsmAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteAsmAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteAsmAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteStages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteStages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteStages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteStageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages",headers=creds) as resp:
           return await resp.json()

async def post_QuoteStages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteStages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company, QuoteNum, QuoteLine, AssemblySeq, StageSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteStage item
   Description: Calls GetByID to retrieve the QuoteStage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param StageSeq: Desc: StageSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company, QuoteNum, QuoteLine, AssemblySeq, StageSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteStage for the service
   Description: Calls UpdateExt to update QuoteStage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param StageSeq: Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteStageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteStages_Company_QuoteNum_QuoteLine_AssemblySeq_StageSeq(Company, QuoteNum, QuoteLine, AssemblySeq, StageSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteStage item
   Description: Call UpdateExt to delete QuoteStage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param StageSeq: Desc: StageSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/QuoteStages(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AssemblySeq + "," + StageSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteAsmListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuoteAsm, whereClauseQuoteAsmAttch, whereClauseQuoteAsmInsp, whereClauseQuoteMtl, whereClauseQuoteMtlAttch, whereClauseQuoteMtlInsp, whereClauseQuoteMtlRefDes, whereClauseQuoteOpr, whereClauseQuoteOprAttch, whereClauseQuoteOprAction, whereClauseQuoteOprActionParam, whereClauseQuoteOprInsp, whereClauseQuoteOpDtl, whereClauseQuoteOprMachParam, whereClauseQuoteAsmRefDes, whereClauseQuoteStage, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteAsm=" + whereClauseQuoteAsm
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteAsmAttch=" + whereClauseQuoteAsmAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteAsmInsp=" + whereClauseQuoteAsmInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteMtl=" + whereClauseQuoteMtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteMtlAttch=" + whereClauseQuoteMtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteMtlInsp=" + whereClauseQuoteMtlInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteMtlRefDes=" + whereClauseQuoteMtlRefDes
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOpr=" + whereClauseQuoteOpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOprAttch=" + whereClauseQuoteOprAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOprAction=" + whereClauseQuoteOprAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOprActionParam=" + whereClauseQuoteOprActionParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOprInsp=" + whereClauseQuoteOprInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOpDtl=" + whereClauseQuoteOpDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteOprMachParam=" + whereClauseQuoteOprMachParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteAsmRefDes=" + whereClauseQuoteAsmRefDes
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteStage=" + whereClauseQuoteStage
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(quoteNum, quoteLine, assemblySeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "quoteNum=" + quoteNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "quoteLine=" + quoteLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assemblySeq=" + assemblySeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRefDesRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRefDesRange
   Description: Creates new QuoteMtlRefDes records based on the QuoteMtl dataset fields.
   OperationID: AddRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AppendDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AppendDetails
   Description: This method takes the records built in BuildAppendDetails that are marked as append
and writes them to the database.  It will return the updated dataset.
   OperationID: AppendDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AppendDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AppendDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildAppendDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildAppendDetails
   Description: This method returns the information that can be appended for approval
   OperationID: BuildAppendDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAppendDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAppendDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpDtlCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpDtlCapability
   Description: Method to call when changing the Capability ID.  This method will update QuoteOpDtl
to see if the labor and burden rates need to be reset.  Blank is a valid entry for
Capability ID.
   OperationID: ChangeOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperAutoReceive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperAutoReceive
   Description: Verification when changing the AutoReceive field
   OperationID: ChangeOperAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperLaborEntryMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperLaborEntryMethod
   Description: Verification when changing the LaborEntryMethod field
   OperationID: ChangeOperLaborEntryMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperLaborEntryMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperLaborEntryMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpDtlOverrideRates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpDtlOverrideRates
   Description: Method to call when changing the Override Rates Flag.  This method will update
QuoteOpDtl with the default labor and burden rates from the appropriate resource
or resource group if the QuoteOpDtl.OverrideRates is set to false.
   OperationID: ChangeOpDtlOverrideRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlOverrideRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlOverrideRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpDtlResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpDtlResourceGrpID
   Description: Method to call when changing the Resource Group ID.  This method will update QuoteOpDtl
with the default labor and burden rates from the new resource group.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeOpDtlResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpDtlResourceID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpDtlResourceID
   Description: Method to call when changing the Resource ID.  This method will update QuoteOpDtl
with the default labor and burden rates from the new resource.  Blank is a valid
entry for Resource ID.
   OperationID: ChangeOpDtlResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpDtlResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpDtlResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperPrimaryProdOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperPrimaryProdOpDtl
   Description: This method defaults/resets the production standards when selecting Primary
Production Operation Detail.
This method should run when the QuoteOpr.PrimaryProdOpDtl field changes.
   OperationID: ChangeOperPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperPrimarySetupOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperPrimarySetupOpDtl
   Description: This method defaults/resets the setup values when selecting Primary
Setup Operation Detail.
This method should run when the QuoteOpr.PrimarySetupOpDtl field changes.
   OperationID: ChangeOperPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMtlPurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMtlPurPoint
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteMtl.PurPoint changes.
   OperationID: ChangeMtlPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperPurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperPurPoint
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteOpr.PurPoint changes.
   OperationID: ChangeOperPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOperVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOperVendorID
   Description: This method updates the vendor related information when the Vendor/Purchase Point
field changes.  It updates the vendor price breaks as well.  This method should run when
the field ttQuoteOpr.VendorNumVendorID changes.
   OperationID: ChangeOperVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOperVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOperVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMtlReqQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMtlReqQty
   Description: Method to call when changing the OpMtlReqQty.
   OperationID: ChangeOpMtlReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMtlReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMtlReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMtlSalvageReqQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMtlSalvageReqQty
   Description: Method to call when changing the QuoteMtl.SalvageQtyPer.
   OperationID: ChangeOpMtlSalvageReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMtlSalvageReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMtlSalvageReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteAsmblQtyPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteAsmblQtyPer
   Description: This methods updates the QuoteAsmbl Required Quantity.
This method should run when the QuoteAsmbl.QtyPer field changes.
   OperationID: ChangeQuoteAsmblQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmblQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmblQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteAsmblValRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteAsmblValRefDes
   Description: Verify that there are no other QuoteMtlRefDes records in the assembly having
the same RefDes value if the QuoteAsmbl.ValRefDes = true. This method should
run before changing the QuoteAsmbl.ValRefDes.
   OperationID: ChangeQuoteAsmblValRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmblValRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmblValRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteAsmReqRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteAsmReqRefDes
   Description: This methods assigns QuoteAsm.RDEndNum field when QuoteAsm.ReqRefDes changes.
This method should run when the QuoteAsm.ReqRefDes changes.
   OperationID: ChangeQuoteAsmReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteAsmReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteAsmReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlEstUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlEstUnitCost
   Description: This methods recalculates the Est Mtl Burden Unit Cost when the
Est Unit Cost value changes.
This method should run when the QuoteMtl.EstUnitCost changes.
   OperationID: ChangeQuoteMtlEstUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlEstUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlEstUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlLinkToContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlLinkToContract
   Description: This method should run when the JobMtl.LinkToContract changes.
   OperationID: ChangeQuoteMtlLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlMtlBurRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlMtlBurRate
   Description: This methods recalculates the Est Mtl Burden Unit Cost when the
Mtl Burden Rate value changes.
This method should run when the QuoteMtl.MtlBurRate changes.
   OperationID: ChangeQuoteMtlMtlBurRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlMtlBurRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlMtlBurRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlMiscCharge(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlMiscCharge
   Description: This method validates if transaction exists and updates fields based on value of Misc. Charge flag.
This method should run when the QuoteMtl.MiscCharge field changes.
   OperationID: ChangeQuoteMtlMiscCharge
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlMiscCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlMiscCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlReqRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlReqRefDes
   Description: This methods assigns QuoteMtl.RDEndNum field when QuoteMtl.ReqRefDes changes.
This method should run when the QuoteMtl.ReqRefDes changes.
   OperationID: ChangeQuoteMtlReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlSalvageMtlBurUnitRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlSalvageMtlBurUnitRate
   Description: This methods recalculates the Salvage Mtl Burden Unit Cost when the
Salvage Mtl Burden Rate value changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeQuoteMtlSalvageMtlBurUnitRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageMtlBurUnitRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageMtlBurUnitRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlSalvagePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlSalvagePartNum
   Description: This methods assigns associated fields when ECOMtl.SalvagePartNum changes.
This method should run when the ECOMtl.SalvagePartNum changes.
   OperationID: ChangeQuoteMtlSalvagePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlSalvageUnitCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlSalvageUnitCredit
   Description: This methods recalculates the Salvage Mtl Burden Unit Cost when the
Salvage Unit Credit value changes.
This method should run when the ECOMtl.SalvageUnitCredit changes.
   OperationID: ChangeQuoteMtlSalvageUnitCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteOprOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteOprOprSeq
   Description: This method will update all of the associated records to the QuoteOpr if the
OprSeq field is changing.
This method should run before changing the QuoteOpr.OprSeq and not when a new record.
   OperationID: ChangeQuoteOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConfigurationAndGetConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConfigurationAndGetConfigType
   Description: This method checks if a part must be configured prior to a GetDetails.
   OperationID: CheckConfigurationAndGetConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigurationAndGetConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigurationAndGetConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_checkQuotePartConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method checkQuotePartConfiguration
   Description: Checks if the Part of the Quote Line needs configuration and return information needed for the configuration call.
   OperationID: checkQuotePartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkQuotePartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkQuotePartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConfiguration
   Description: This method checks if a part must be configured prior to a GetDetails.
   OperationID: CheckConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConfigurationAndGetConfigInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConfigurationAndGetConfigInfo
   Description: This method checks if a part must be configured prior to a GetDetails and retrieves information related to the configuration.
   OperationID: CheckConfigurationAndGetConfigInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigurationAndGetConfigInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigurationAndGetConfigInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOperPrimaryProdOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOperPrimaryProdOpDtl
   Description: This method validated the value of Primary Production Operation Detail.
This method should run when the QuoteOpr.PrimaryProdOpDtl is changing.
   OperationID: CheckOperPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOperPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOperPrimarySetupOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOperPrimarySetupOpDtl
   Description: This method validated the value of Primary Setup Operation Detail.
This method should run when the QuoteOpr.PrimarySetupOpDtl is changing.
   OperationID: CheckOperPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOperPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartErrors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartErrors
   Description: This method runs through a quote's BOM and returns a list of assembly and/or
materials that are on hold or inactive.  Quote cannot be engineered or Quoted
until these errors are taken care of
   OperationID: CheckPartErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: The method is to be run on leave of the PartNum, Revision fields before the
GetPartInfo or Update methods are run.  This returns all the questions that
need to be asked before a part can be changed.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CollapseAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CollapseAssembly
   Description: Collapses any single Quote Assembly except Assembly 0
   OperationID: CollapseAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollapseAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollapseAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteAsmChildDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteAsmChildDelete
   Description: Deletes the QuoteAsm child records
   OperationID: QuoteAsmChildDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteAsmChildDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteAsmChildDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAllAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAllAssembly
   Description: The method deletes all assemblies and their subassemblies, materials and operations
while leaving the base assembly sequence alone.
   OperationID: DeleteAllAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAllAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRefDesRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRefDesRange
   Description: Deletes QuoteMtlRefDes records based on the QuoteMtl dataset fields.
   OperationID: DeleteRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableSupplierPriceList(epicorHeaders = None):
   """  
   Summary: Invoke method EnableSupplierPriceList
   Description: This method returns whether or not the supplier price list option
is enabled.  This is based on security rights for the user.
   OperationID: EnableSupplierPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSupplierPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_FindAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindAsm
   OperationID: FindAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAsmOprInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAsmOprInfo
   Description: This method updates the related operation description when the RelatedOperation field
changes. To be run before update.
   OperationID: GetAsmOprInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAsmOprInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsmOprInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAsmPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAsmPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum or Revision field
changes. To be run before update. CheckPrePartInfo should be run first
   OperationID: GetAsmPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAsmPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsmPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartAndConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBasePartForConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlConfigPartRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlConfigPartRev
   OperationID: GetMtlConfigPartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlConfigPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlConfigPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlConfigPartRevAndConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlConfigPartRevAndConfigType
   OperationID: GetMtlConfigPartRevAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlConfigPartRevAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlConfigPartRevAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTreeByRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTreeByRef
   Description: Same as GetDataSetForTree but expects ref QuoteAsmTableset to improve performance within kinetic when merging large volumes of data.
            
This methods will return the dataset for QuoteAsm.  The method will return the
records related to the assembly provided and the first child level assemblies related to
the input inputted assembly.
   OperationID: GetDatasetForTreeByRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return the dataset for QuoteAsm.  The method will return the
records related to the assembly provided and the first child level assemblies related to
the input inputted assembly.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTreeRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTreeRefresh
   Description: This methods will return the dataset for QuoteAsm.  The method will return the
records related to all the assemblies specified in assemblySeqList
   OperationID: GetDatasetForTreeRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetails
   Description: This method retrieves the manufacturing details from a source file.  The source file
will either be a Quote, a Job, or a Method (Part).  The assembly records will
be created regardless if the part is in error or not.  If there are errors, the
quote cannot be "quoted" unless all parts are fixed.  To find the parts in error
run CheckPartErrors
   OperationID: GetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlBuyItInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlBuyItInfo
   Description: This method updates Vendor and LeadTime when BuyIt is checked
   OperationID: GetMtlBuyItInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlBuyItInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlBuyItInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlDirectInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlDirectInfo
   Description: This method updates Vendor and LeadTime when BuyIt is checked
   OperationID: GetMtlDirectInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlDirectInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlDirectInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlOprInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlOprInfo
   Description: This method defaults the EstScrap fields when the QuoteMtl.RelatedOperation changes
   OperationID: GetMtlOprInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlOprInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlOprInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteMtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteMtlPartNum
   OperationID: CheckQuoteMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum field changes.
To be run after partNum changes but before update. CheckPrePartInfo should be run first
   OperationID: GetMtlPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlVendorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlVendorInfo
   Description: This method defaults the Vendor fields when the VendorNumVendorID field is changed
   OperationID: GetMtlVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAssembly
   Description: This method creates a new Assembly after prompting for the AsemblySeq and BOMLevel
as well as the QuoteLine and QuoteNum fields. This is to replace the standard GetNewQuoteAsm
   OperationID: GetNewAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOperation
   Description: This method creates a new Operation after prompting for the SubConType as well as the
AssemblySeq, QuoteLine and QuoteNum fields. This is to replace the standard GetNewQuoteOpr
   OperationID: GetNewOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOprOpCodeInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOprOpCodeInfo
   Description: This method defaults the OpStd information when the OpCode field changes.
Updates the burden rates as well.
   OperationID: GetOprOpCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprOpCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprOpCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOprOpStdInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOprOpStdInfo
   Description: This method defaults Operation Standard information when OpStdId changes
   OperationID: GetOprOpStdInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprOpStdInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprOpStdInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOprPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOprPartInfo
   Description: This method updates the dataset with Part Defaults when the PartNum field changes.
To be run after partNum changes but before update. CheckPrePartInfo should be run first
   OperationID: GetOprPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOprStdFormatInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOprStdFormatInfo
   Description: This method updates the dataset after the StdFormat field changes.  Can be run on the ColumnChanged event
   OperationID: GetOprStdFormatInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOprStdFormatInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOprStdFormatInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteEngUIDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteEngUIDefaults
   Description: Return separated list of values for use in QuoteEng:
AllowPurchasingInfo = Security.CheckSecurityAccess("bo.Part.AllowPurchasingInfo")
PreventQQChange = EQSyst.PreventQQChange
SiteExternalMES = PlantConfCtrl.ExternalMES
   OperationID: GetQuoteEngUIDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteEngUIDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMAsm
   Description: This methods allows for the insertion of an engineering assembly for drag/drop functionality,
validates a QuoteAsm record exists for the parent
   OperationID: InsertBOMAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMMtl
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates a JobAsmbl record exists for the parent
   OperationID: InsertBOMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMOper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMOper
   Description: This methods allows for the insertion of an engineering operation for drag/drop functionality,
validates a JobAsmbl record exists for the parent
   OperationID: InsertBOMOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertMaterial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertMaterial
   Description: This methods allows for the insertion on a material for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlCapability
   Description: This method allows for the insertion of Capability on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlResource
   Description: This method allows for the insertion of Resource on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlResourceGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlResourceGrp
   Description: This method allows for the insertion of Resource Group on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertOpDtlResourceGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResourceGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResourceGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperationOP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperationOP
   Description: This methods allows for the insertion of an operation for drag/drop functionality
using operation code as input.  This would eventually replace the original InsertOperation
method where work center code is the input.
   OperationID: InsertOperationOP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperCapability
   Description: This method allows for the insertion of Capability on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperResGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperResGroup
   Description: This method allows for the insertion of ResourceGroup on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperResource
   Description: This method allows for the insertion of Resource on an assembly to create
QuoteOpr/QuoteOpDtl for drag/drop functionality.
   OperationID: InsertOperResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertSubAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertSubAssembly
   Description: This methods allows for the insertion of a subassembly for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertSubAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertSubAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertSubAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertNewSubAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertNewSubAssembly
   Description: This methods allows for the insertion of a subassembly for drag/drop functionality,
validates a QuoteAsm record exists and the part is valid.
   OperationID: InsertNewSubAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertNewSubAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertNewSubAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLinkToContractData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLinkToContractData
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidateLinkToContractData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLinkToContractData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLinkToContractData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChangeJobAsmblParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChangeJobAsmblParent
   Description: This method validates validates the new Parent field
   OperationID: CheckChangeJobAsmblParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeJobAsmblParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeJobAsmblParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobAsmblParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobAsmblParent
   Description: This method validates the new Parent field and populates defaults associated with the Parent.
This method should run when the JobAsmbl.Parent field changes.
   OperationID: ChangeJobAsmblParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobAsmblParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsmblParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteOprInitSNReqSubCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteOprInitSNReqSubCon
   Description: Method required to set the initial value of QuoteOpr.SNRequiredSubConShip
   OperationID: QuoteOprInitSNReqSubCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteOprInitSNReqSubCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteOprInitSNReqSubCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSNReqValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSNReqValues
   Description: This method updates the columns SNRequiredOpr and SNRequiredSubConShip when the main Part
changes. If the new part number is not serial tracked and those fields were set as true previuosly, they must be set to false.
   OperationID: ValidateSNReqValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSNReqValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSNReqValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInspection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartToLinkToContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartToLinkToContract
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidatePartToLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartToLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartToLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshMtlPriceBreak(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshMtlPriceBreak
   Description: This method refreshes the QuoteMtl PBrkQty and PBrkCost fields after
VendPart and VendPBrk tables have been updated. It will also update the
LeadTime and Unit Cost fields as well.
   OperationID: RefreshMtlPriceBreak
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshMtlPriceBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshMtlPriceBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshOprPriceBreak(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshOprPriceBreak
   Description: This method refreshes the QuoteOpr PBrkQty and PBrkCost fields after
VendPart and VendPBrk tables have been updated. It will also update the
LeadTime and Unit Cost fields as well.
   OperationID: RefreshOprPriceBreak
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshOprPriceBreak_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOprPriceBreak_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResequenceMaterial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResequenceMaterial
   Description: This method resequences Material for an assembly by sequence, part or bubble
   OperationID: ResequenceMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResequenceOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResequenceOperations
   Description: This method resequences the operations of an assembly by 10's
   OperationID: ResequenceOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteOprIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteOprIUM
   Description: procedure for changing QuoteOpr.IUM field
   OperationID: ChangeQuoteOprIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteOprQtyPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteOprQtyPer
   Description: procedure for changing QuoteOpr.QtyPer field
   OperationID: ChangeQuoteOprQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlIUM
   Description: procedure for changing QuoteMtl.IUM field
   OperationID: ChangeQuoteMtlIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteMtlSalvageUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteMtlSalvageUM
   Description: procedure for changing QuoteMtl.SalvageUM field
   OperationID: ChangeQuoteMtlSalvageUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteMtlSalvageUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteMtlSalvageUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteOprSNRequiredOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteOprSNRequiredOpr
   Description: Validates SNRequiredOpr flag to avoid to set it false if the prior operation has the flag set to true
The flag cannot be set to true if the part is not serial tracked also.
   OperationID: ChangeQuoteOprSNRequiredOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteOprSNRequiredOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteOprSNRequiredOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubcontractPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubcontractPartNum
   Description: Check if SNRequiredOpr column is enabled/disabled on Subcontract Detail panel on UI
   OperationID: ChangeSubcontractPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubcontractPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubcontractPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_JobPartBeforeGetNew(epicorHeaders = None):
   """  
   Summary: Invoke method JobPartBeforeGetNew
   Description: Validates if JobHead.PartNum is serial tracked, additional JobParts cannot be added.
   OperationID: JobPartBeforeGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobPartBeforeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetProjectRoles(epicorHeaders = None):
   """  
   Summary: Invoke method GetProjectRoles
   Description: Returns list of Project Roles
   OperationID: GetProjectRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteMtlIsMtlConfigurationOn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteMtlIsMtlConfigurationOn
   Description: After Material was configured we need to check if was success to display the correct Materials Tree Context Menu option (Configure or Configuration)
   OperationID: GetQuoteMtlIsMtlConfigurationOn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteMtlIsMtlConfigurationOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteMtlIsMtlConfigurationOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGetDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGetDetails
   Description: This method should be called right before the GetDetails method.  It necessary,
it'll return a question on resequencing assembly's while getting details.
The answer will be sent as a parameter to the GetDetails method.
This method will also return a BasePartNum and BaseRevisionNum.  If the BasePartNum
isn't null then use this as the default part number for GetDetails.
This is called from GetDetailsEntry
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindQuoteMtlByPLMMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindQuoteMtlByPLMMtlSeq
   Description: Allows PLM Users to get QuoteMtl's AsmSeq and MtlSeq by sending the unique-per-line value PLMMtlSeq
   OperationID: FindQuoteMtlByPLMMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindQuoteMtlByPLMMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindQuoteMtlByPLMMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSetQuoteAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSetQuoteAsm
   Description: Call this method when the QuoteAsm attribute set changes
   OperationID: OnChangingAttributeSetQuoteAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSetQuoteMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSetQuoteMtl
   Description: Call this method when the QuoteMtl attribute set changes
   OperationID: OnChangingAttributeSetQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSetQuoteOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSetQuoteOpr
   Description: Call this method when the QuoteOpr attribute set changes
   OperationID: OnChangingAttributeSetQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPiecesQuoteMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPiecesQuoteMtl
   Description: Call this method when the QuoteMtl Number Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPiecesQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPiecesQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPiecesQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPiecesQuoteOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPiecesQuoteOpr
   Description: Call this method when the QuoteOpr Number Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPiecesQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPiecesQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPiecesQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMtlRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMtlRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingMtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingQuoteOprRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingQuoteOprRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingQuoteOprRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingQuoteOprRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingQuoteOprRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSalvageRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSalvageRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSalvageRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteAsm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteAsmAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteAsmAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteAsmInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteAsmInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteMtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteMtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteMtlInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteMtlInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteMtlRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteMtlRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMtlRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOprAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOprAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOprAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOprAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOprActionParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOprActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprActionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOprInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOprInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOpDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteOprMachParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteOprMachParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteOprMachParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteOprMachParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteOprMachParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteAsmRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteAsmRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteAsmRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteAsmRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteAsmRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteStage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteStage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteAsmSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteAsmAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteAsmInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteAsmListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRefDesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteAsmRefDesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteAsmRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteAsmRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteMtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteMtlInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRefDesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteMtlRefDesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteMtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOpDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOpDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprActionParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprMachParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprMachParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteOprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteOprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteStageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteStageRow] = obj["value"]
      pass

class Erp_Tablesets_QuoteAsmAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteAsmInsp record within the QuoteNum/QuoteLine/AssemblySeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production Quantity required for this assembly per one of it's Parent Part.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for this assembly. Use the Part.IUM as a default.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  """  
      self.Child:int = obj["Child"]
      """  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  QutoeAsm.PartNum of the Parent Assembly  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  QuoteAsm.RevisionNum of the Parent Assembly  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  QuoteAsm.Description of Parent assmebly  """  
      self.ProcessingDetails:bool = obj["ProcessingDetails"]
      """  Boolean to indicate GetDetails has started  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  Clone of the Parent field (.Net keyword issue)  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  Clone of the Child field (.Net keyword issue)  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  Add assembly as "Sub"assembly or "Asm"bly  """  
      self.OverrideNextAsmSeq:bool = obj["OverrideNextAsmSeq"]
      """  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production Quantity required for this assembly per one of it's Parent Part.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for this assembly. Use the Part.IUM as a default.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  """  
      self.Child:int = obj["Child"]
      """  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  Clone of the Child field (.Net keyword issue)  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.OverrideNextAsmSeq:bool = obj["OverrideNextAsmSeq"]
      """  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  Clone of the Parent field (.Net keyword issue)  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  QuoteAsm.Description of Parent assmebly  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  QutoeAsm.PartNum of the Parent Assembly  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  QuoteAsm.RevisionNum of the Parent Assembly  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part  """  
      self.ProcessingDetails:bool = obj["ProcessingDetails"]
      """  Boolean to indicate GetDetails has started  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  Add assembly as "Sub"assembly or "Asm"bly  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineSmartString:str = obj["QuoteLineSmartString"]
      self.QuoteLineGroupSeq:int = obj["QuoteLineGroupSeq"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteLineSysRowID:str = obj["QuoteLineSysRowID"]
      self.QuoteLineSmartStringProcessed:bool = obj["QuoteLineSmartStringProcessed"]
      self.QuoteLineReadyToQuote:bool = obj["QuoteLineReadyToQuote"]
      self.QuoteLineContractID:str = obj["QuoteLineContractID"]
      self.QuoteLineKitFlag:str = obj["QuoteLineKitFlag"]
      self.QuoteLineExternalMES:bool = obj["QuoteLineExternalMES"]
      self.QuoteNumQuoted:bool = obj["QuoteNumQuoted"]
      self.QuoteNumQuoteClosed:bool = obj["QuoteNumQuoteClosed"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.QuoteNumCustNum:int = obj["QuoteNumCustNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteMtlInsp record within the QuoteNum/QuoteLine/AssemblySeq/MtlSeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  """  
      self.Description:str = obj["Description"]
      """  Description of the material. Cannot be blank  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  """  
      self.IUM:str = obj["IUM"]
      """  The issue/usage unit of measure for this material.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvaged material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Quote Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Quote Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.Class:str = obj["Class"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkQty01:int = obj["PBrkQty01"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty02:int = obj["PBrkQty02"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty03:int = obj["PBrkQty03"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty04:int = obj["PBrkQty04"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty05:int = obj["PBrkQty05"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty06:int = obj["PBrkQty06"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty07:int = obj["PBrkQty07"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty08:int = obj["PBrkQty08"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty09:int = obj["PBrkQty09"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty10:int = obj["PBrkQty10"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.PLMMtlSeq:int = obj["PLMMtlSeq"]
      """  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AddrList:str = obj["AddrList"]
      """  Delimited list of Address fields in Company format  """  
      self.AutoSetChkDirect:bool = obj["AutoSetChkDirect"]
      """  This field will tell if the Direct checkbox will be automatically set. If using a NonPartMaster then this field will be set to FALSE. Otherwise if QtyBearing is Yes then this field will be set to TRUE.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  Base Unit of Measure  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This field is used as and internal flag on BO to enable/disable FixedQty column on UI form.  """  
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      """  IsMtlRevisionApproved  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PBImage:str = obj["PBImage"]
      """  Indicates if theres a price break available and if its expired  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      """  Description from OpMaster of the QuoteOpr.OpCode  """  
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  Salvage Part Base UOM  """  
      self.SalvagePartTrackMulti:bool = obj["SalvagePartTrackMulti"]
      """  Salvage Part Track Dimension Setting  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Scrap Unit of Measure  """  
      self.VendorAddress:str = obj["VendorAddress"]
      """  Vendor address formatted  """  
      self.DispPlanningNumberOfPieces:int = obj["DispPlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.DispSalvagePlanningNumberOfPieces:int = obj["DispSalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvageAttrClassID:str = obj["SalvageAttrClassID"]
      """  ID of related Attribute Class.  """  
      self.SalvageTrackInventoryAttributes:bool = obj["SalvageTrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.SalvageTrackInventoryByRevision:bool = obj["SalvageTrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.   System assigned.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Used to link back to the QuoteLine.   System assigned.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Used to link back to the QuoteAsmbl record.  System assigned.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Used to link back to the QuoteOpr record.  System assigned.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies the QuoteOpDtl.  System assigned.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  The labor rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.OverrideRates:bool = obj["OverrideRates"]
      """  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      self.OperOpStdID:str = obj["OperOpStdID"]
      """  The Operation Standard ID stored in QuoteOpr.  """  
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  Indicates if primary production operation.  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  Indicates if primary setup operation.  """  
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.SubContract:bool = obj["SubContract"]
      """  Flag for sub contract  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter.  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteOprInsp record within the QuoteNum/QuoteLine/AssemblySeq/OprSeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.MachParamSeq:int = obj["MachParamSeq"]
      """  MachParamSeq  """  
      self.RequestCode:str = obj["RequestCode"]
      """  RequestCode  """  
      self.MachineNum:str = obj["MachineNum"]
      """  MachineNum  """  
      self.ToolNum:str = obj["ToolNum"]
      """  ToolNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.ParamNum:int = obj["ParamNum"]
      """  ParamNum  """  
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      """  ParamUpperLimit  """  
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      """  ParamNominalValue  """  
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      """  ParamLowerLimit  """  
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      """  ParamDelayValue  """  
      self.SpecEnable:bool = obj["SpecEnable"]
      """  SpecEnable  """  
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      """  SpecControlAlarm  """  
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      """  SpecRunAlarm  """  
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      """  ProcSpecAlarm  """  
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      """  ProcControlAlarm  """  
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      """  PartQualSpecEnable  """  
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      """  PartQualControlEnable  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue Unit of Measure. Applicable only when SubContract = Yes  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description of item to be sent to subcontractor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for quote operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.RunQty:int = obj["RunQty"]
      """  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.StageNumber:str = obj["StageNumber"]
      """  StageNumber  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.AddrList:str = obj["AddrList"]
      """  Vendor Address  """  
      self.APSAltOpDesc:str = obj["APSAltOpDesc"]
      self.APSNextOpDesc:str = obj["APSNextOpDesc"]
      self.APSPrepOpDesc:str = obj["APSPrepOpDesc"]
      self.AutoReceive:bool = obj["AutoReceive"]
      self.DspQtyIUM:str = obj["DspQtyIUM"]
      """  Used to display selected UOM next to unit cost field  """  
      self.EnableAutoRec:bool = obj["EnableAutoRec"]
      """  Indicates whether to enable the AutoReceive field  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  This field is used as a flag to enable/disable the controls binded to SNRequiredOpr column in UI forms.  """  
      self.EnableSNSubConShip:bool = obj["EnableSNSubConShip"]
      """  This field is used as a flag for SNRequiredSubConShip column to determine when to enable/disable it on UI form.  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      self.HoursPerMachine:int = obj["HoursPerMachine"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PBImage:str = obj["PBImage"]
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group Description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.VendorAddress:str = obj["VendorAddress"]
      """  Vendor address formatted  """  
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Stage is associated with.  """  
      self.StageSeq:int = obj["StageSeq"]
      """  A sequence number which uniquely identifies stage record within the stage set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.StageNumberDescription:str = obj["StageNumberDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddRefDesRange_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipAsmSeq
   ipMtlSeq
   ipPrefix
   ipStartNum
   ipEndNum
   ipSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number  """  
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      """  The Quote Assembly  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The Quote Material Seq  """  
      self.ipPrefix:str = obj["ipPrefix"]
      """  The Prefix to be used to delete Reference Designators  """  
      self.ipStartNum:int = obj["ipStartNum"]
      """  The Starting Number to delete Reference Designators  """  
      self.ipEndNum:int = obj["ipEndNum"]
      """  The Ending Number to delete Reference Designators  """  
      self.ipSuffix:str = obj["ipSuffix"]
      """  The Suffix to be used to delete Reference Designators  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class AddRefDesRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AppendDetails_input:
   """ Required : 
   ds
   targetQuote
   targetLine
   targetAsm
   sourceFile
   keyOne
   keyTwo
   keyThree
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QtAppendTableset] = obj["ds"]
      self.targetQuote:int = obj["targetQuote"]
      """  Target Quote  """  
      self.targetLine:int = obj["targetLine"]
      """  Target QuoteLine  """  
      self.targetAsm:int = obj["targetAsm"]
      """  Target Quote AssemblySeq  """  
      self.sourceFile:str = obj["sourceFile"]
      """  Indicates where the details are being appended from.  Either Quote,
           Job or Method  """  
      self.keyOne:str = obj["keyOne"]
      """  Unique key field one for Job or Method source  """  
      self.keyTwo:str = obj["keyTwo"]
      """  Unique key field two for Method source  """  
      self.keyThree:str = obj["keyThree"]
      """  Unique key field two for Method source  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class AppendDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildAppendDetails_input:
   """ Required : 
   sourceFile
   keyOne
   keyTwo
   keyThree
   targetQuote
   targetLine
   targetAsm
   vShipByDate
   """  
   def __init__(self, obj):
      self.sourceFile:str = obj["sourceFile"]
      """  Source of the append details, Quote, Job or Method  """  
      self.keyOne:str = obj["keyOne"]
      """  First key field of source  """  
      self.keyTwo:str = obj["keyTwo"]
      """  Second key field of source  """  
      self.keyThree:str = obj["keyThree"]
      """  Third key field of source  """  
      self.targetQuote:int = obj["targetQuote"]
      """  Target Quote Num  """  
      self.targetLine:int = obj["targetLine"]
      """  Target Line Number  """  
      self.targetAsm:int = obj["targetAsm"]
      """  Target Assembly  """  
      self.vShipByDate:str = obj["vShipByDate"]
      """  used to correctly calculate Revision for Pahntom Mtls on Append Details.  """  
      pass

class BuildAppendDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QtAppendTableset] = obj["returnObj"]
      pass

class ChangeJobAsmblParent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeJobAsmblParent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMtlPurPoint_input:
   """ Required : 
   ProposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.ProposedPurPoint:str = obj["ProposedPurPoint"]
      """  The proposed Purchase Point  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeMtlPurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpDtlCapability_input:
   """ Required : 
   ProposedCapID
   ds
   """  
   def __init__(self, obj):
      self.ProposedCapID:str = obj["ProposedCapID"]
      """  The proposed Capability ID  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpDtlCapability_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpDtlOverrideRates_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpDtlOverrideRates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpDtlResourceGrpID_input:
   """ Required : 
   ProposedResGrpID
   ds
   """  
   def __init__(self, obj):
      self.ProposedResGrpID:str = obj["ProposedResGrpID"]
      """  The proposed Resource Group ID  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpDtlResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpDtlResourceID_input:
   """ Required : 
   ProposedResourceID
   ds
   """  
   def __init__(self, obj):
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  The proposed Resource ID  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpDtlResourceID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMtlReqQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpMtlReqQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMtlSalvageReqQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOpMtlSalvageReqQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperAutoReceive_input:
   """ Required : 
   iAutoReceive
   ds
   """  
   def __init__(self, obj):
      self.iAutoReceive:bool = obj["iAutoReceive"]
      """  Proposed value for AutoReceive field  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperAutoReceive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperLaborEntryMethod_input:
   """ Required : 
   iLaborEntryMethod
   ds
   """  
   def __init__(self, obj):
      self.iLaborEntryMethod:str = obj["iLaborEntryMethod"]
      """  Proposed value for LaborEntryMethod field  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperLaborEntryMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperPrimaryProdOpDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperPrimaryProdOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperPrimarySetupOpDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperPrimarySetupOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperPurPoint_input:
   """ Required : 
   ProposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.ProposedPurPoint:str = obj["ProposedPurPoint"]
      """  The proposed Purchase Point  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperPurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOperVendorID_input:
   """ Required : 
   ProposedVendorID
   ds
   """  
   def __init__(self, obj):
      self.ProposedVendorID:str = obj["ProposedVendorID"]
      """  The proposed Vendor ID  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeOperVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteAsmReqRefDes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteAsmReqRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteAsmblQtyPer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteAsmblQtyPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteAsmblValRefDes_input:
   """ Required : 
   ipProposedValResDes
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValResDes:bool = obj["ipProposedValResDes"]
      """  The new proposed QuoteAsmbl.ValRefDes value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteAsmblValRefDes_output:
   def __init__(self, obj):
      pass

class ChangeQuoteMtlEstUnitCost_input:
   """ Required : 
   ipProposedEstUnitCost
   ds
   """  
   def __init__(self, obj):
      self.ipProposedEstUnitCost:int = obj["ipProposedEstUnitCost"]
      """  The new proposed QuoteMtl.MtlBurRate value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlEstUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlIUM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlLinkToContract_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlLinkToContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlMiscCharge_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlMiscCharge_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlMtlBurRate_input:
   """ Required : 
   ipProposedMtlBurRate
   ds
   """  
   def __init__(self, obj):
      self.ipProposedMtlBurRate:int = obj["ipProposedMtlBurRate"]
      """  The new proposed QuoteMtl.MtlBurRate value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlMtlBurRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlReqRefDes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlReqRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlSalvageMtlBurUnitRate_input:
   """ Required : 
   ipProposedSalvageMtlBurRate
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvageMtlBurRate:int = obj["ipProposedSalvageMtlBurRate"]
      """  The new proposed ECOMtl.SalvageMtlBurRate value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlSalvageMtlBurUnitRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlSalvagePartNum_input:
   """ Required : 
   ipProposedSalvagePartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvagePartNum:str = obj["ipProposedSalvagePartNum"]
      """  The new proposed ECOMtl.SalvagePartNum value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlSalvagePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlSalvageUM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlSalvageUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteMtlSalvageUnitCredit_input:
   """ Required : 
   ipProposedSalvageUnitCredit
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvageUnitCredit:int = obj["ipProposedSalvageUnitCredit"]
      """  The new proposed ECOMtl.SalvageUnitCredit value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteMtlSalvageUnitCredit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteOprIUM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteOprIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteOprOprSeq_input:
   """ Required : 
   ipProposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.ipProposedOprSeq:int = obj["ipProposedOprSeq"]
      """  The new proposed QuoteOpr.OprSeq value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteOprOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteOprQtyPer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteOprQtyPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteOprSNRequiredOpr_input:
   """ Required : 
   ipProposedSNRequired
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSNRequired:bool = obj["ipProposedSNRequired"]
      """  The new proposed QuoteAsm.SNRequiredOpr value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeQuoteOprSNRequiredOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSubcontractPartNum_input:
   """ Required : 
   ipProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPartNum:str = obj["ipProposedPartNum"]
      """  The new proposed QuoteOpr.PartNum value  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ChangeSubcontractPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckChangeJobAsmblParent_input:
   """ Required : 
   ipNewParent
   ds
   """  
   def __init__(self, obj):
      self.ipNewParent:int = obj["ipNewParent"]
      """  New Parent value to check against  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class CheckChangeJobAsmblParent_output:
   def __init__(self, obj):
      pass

class CheckConfigurationAndGetConfigInfo_input:
   """ Required : 
   relatedToTable
   relatedToSysRowID
   sourcePart
   sourceRevision
   findRevision
   foreignTable
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.relatedToTable:str = obj["relatedToTable"]
      """  Related To File  """  
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  The job on which the configuration should be saved.  """  
      self.sourcePart:str = obj["sourcePart"]
      """  Part Num to get details from (populated when sourceFile = "Method")  """  
      self.sourceRevision:str = obj["sourceRevision"]
      """  Revision number to get details from (populated when sourceFile = "Method")  """  
      self.findRevision:bool = obj["findRevision"]
      """  Foreign row  """  
      self.foreignTable:str = obj["foreignTable"]
      """  Foreign row  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      """  Foreign row SysRowID  """  
      pass

class CheckConfigurationAndGetConfigInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.foreignTable:str = obj["parameters"]
      self.foreignSysRowID:str = obj["parameters"]
      self.configurationExists:bool = obj["configurationExists"]
      self.canGetDetails:bool = obj["canGetDetails"]
      self.needsConfiguration:bool = obj["needsConfiguration"]
      self.configureRevision:str = obj["parameters"]
      self.reasonMessage:str = obj["parameters"]
      self.warningMsg:bool = obj["warningMsg"]
      self.isNIC:bool = obj["isNIC"]
      self.structTag:str = obj["parameters"]
      self.ruleTag:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      self.kbConfigProdID:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckConfigurationAndGetConfigType_input:
   """ Required : 
   relatedToTable
   relatedToSysRowID
   sourcePart
   sourceRevision
   findRevision
   foreignTable
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.relatedToTable:str = obj["relatedToTable"]
      """  Related To File  """  
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  The job on which the configuration should be saved.  """  
      self.sourcePart:str = obj["sourcePart"]
      """  Part Num to get details from (populated when sourceFile = "Method")  """  
      self.sourceRevision:str = obj["sourceRevision"]
      """  Revision number to get details from (populated when sourceFile = "Method")  """  
      self.findRevision:bool = obj["findRevision"]
      """  Foreign row  """  
      self.foreignTable:str = obj["foreignTable"]
      """  Foreign row  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      """  Foreign row SysRowID  """  
      pass

class CheckConfigurationAndGetConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.foreignTable:str = obj["parameters"]
      self.foreignSysRowID:str = obj["parameters"]
      self.configurationExists:bool = obj["configurationExists"]
      self.canGetDetails:bool = obj["canGetDetails"]
      self.needsConfiguration:bool = obj["needsConfiguration"]
      self.configureRevision:str = obj["parameters"]
      self.reasonMessage:str = obj["parameters"]
      self.warningMsg:bool = obj["warningMsg"]
      self.isNIC:bool = obj["isNIC"]
      self.structTag:str = obj["parameters"]
      self.ruleTag:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckConfiguration_input:
   """ Required : 
   relatedToTable
   relatedToSysRowID
   sourcePart
   sourceRevision
   findRevision
   foreignTable
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.relatedToTable:str = obj["relatedToTable"]
      """  Related To File  """  
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  The job on which the configuration should be saved.  """  
      self.sourcePart:str = obj["sourcePart"]
      """  Part Num to get details from (populated when sourceFile = "Method")  """  
      self.sourceRevision:str = obj["sourceRevision"]
      """  Revision number to get details from (populated when sourceFile = "Method")  """  
      self.findRevision:bool = obj["findRevision"]
      self.foreignTable:str = obj["foreignTable"]
      """  Foreign row  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      """  Foreign row SysRowID  """  
      pass

class CheckConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.foreignTable:str = obj["parameters"]
      self.foreignSysRowID:str = obj["parameters"]
      self.configurationExists:bool = obj["configurationExists"]
      self.canGetDetails:bool = obj["canGetDetails"]
      self.needsConfiguration:bool = obj["needsConfiguration"]
      self.configureRevision:str = obj["parameters"]
      self.reasonMessage:str = obj["parameters"]
      self.warningMsg:bool = obj["warningMsg"]
      self.isNIC:bool = obj["isNIC"]
      self.structTag:str = obj["parameters"]
      self.ruleTag:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOperPrimaryProdOpDtl_input:
   """ Required : 
   ds
   ipPrimaryProdOpDtl
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.ipPrimaryProdOpDtl:int = obj["ipPrimaryProdOpDtl"]
      """  The new PrimaryProdOpDtl value to change to  """  
      pass

class CheckOperPrimaryProdOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckOperPrimarySetupOpDtl_input:
   """ Required : 
   ds
   ipPrimarySetupOpDtl
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.ipPrimarySetupOpDtl:int = obj["ipPrimarySetupOpDtl"]
      """  The new PrimarySetupOpDtl value to change to  """  
      pass

class CheckOperPrimarySetupOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPartErrors_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  QuoteLine, 0 for all lines, otherwise only looks a specific line  """  
      pass

class CheckPartErrors_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.runOutWarnings:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   partNum
   sourceTable
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part  """  
      self.sourceTable:str = obj["sourceTable"]
      """  The table that caused this method to be called  """  
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  sys row DI of the source table - this is needed for the product configurator logic  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMessage:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      self.productConfiguratorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckQuoteMtlPartNum_input:
   """ Required : 
   ds
   ipProposedPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.ipProposedPartNum:str = obj["ipProposedPartNum"]
      """  Identifies the PartNum to validate  """  
      pass

class CheckQuoteMtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CollapseAssembly_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipAsmSeq
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      pass

class CollapseAssembly_output:
   def __init__(self, obj):
      pass

class DeleteAllAssembly_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number of the assemblies  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Assembly Line Number  """  
      pass

class DeleteAllAssembly_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteRefDesRange_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipAsmSeq
   ipMtlSeq
   ipPrefix
   ipStartNum
   ipEndNum
   ipSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number  """  
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      """  The Quote Assembly  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The Quote Material Seq  """  
      self.ipPrefix:str = obj["ipPrefix"]
      """  The Prefix to be used to delete Reference Designators  """  
      self.ipStartNum:int = obj["ipStartNum"]
      """  The Starting Number to delete Reference Designators  """  
      self.ipEndNum:int = obj["ipEndNum"]
      """  The Ending Number to delete Reference Designators  """  
      self.ipSuffix:str = obj["ipSuffix"]
      """  The Suffix to be used to delete Reference Designators  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class DeleteRefDesRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EnableSupplierPriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lEnableSupplierPriceList:bool = obj["lEnableSupplierPriceList"]
      pass

      """  output parameters  """  

class Erp_Tablesets_QtAppendTableset:
   def __init__(self, obj):
      self.QtMtlApp:list[Erp_Tablesets_QtMtlAppRow] = obj["QtMtlApp"]
      self.QtOprApp:list[Erp_Tablesets_QtOprAppRow] = obj["QtOprApp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QtMtlAppRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  """  
      self.Description:str = obj["Description"]
      """  Description of the material. Cannot be blank  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  """  
      self.IUM:str = obj["IUM"]
      """  The issue/usage unit of measure for this material.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvaged material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Quote Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Quote Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.Class:str = obj["Class"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkQty01:int = obj["PBrkQty01"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty02:int = obj["PBrkQty02"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty03:int = obj["PBrkQty03"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty04:int = obj["PBrkQty04"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty05:int = obj["PBrkQty05"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty06:int = obj["PBrkQty06"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty07:int = obj["PBrkQty07"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty08:int = obj["PBrkQty08"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty09:int = obj["PBrkQty09"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty10:int = obj["PBrkQty10"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.Append:bool = obj["Append"]
      """  Indicates whether to append QuoteMtl record or not  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.AltMethod:str = obj["AltMethod"]
      """  The alternate method for the material.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QtOprAppRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue Unit of Measure. Applicable only when SubContract = Yes  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description of item to be sent to subcontractor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for quote operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.RunQty:int = obj["RunQty"]
      """  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      self.APSNextOp:int = obj["APSNextOp"]
      self.APSAltOp:int = obj["APSAltOp"]
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      self.APSCycleTime:int = obj["APSCycleTime"]
      self.APSConstantTime:int = obj["APSConstantTime"]
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      self.APSContainerSize:int = obj["APSContainerSize"]
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      self.APSMaxLength:int = obj["APSMaxLength"]
      self.APSTransferTime:int = obj["APSTransferTime"]
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      self.APSOperationClass:str = obj["APSOperationClass"]
      self.APSAuxResource:str = obj["APSAuxResource"]
      self.APSAddResource:str = obj["APSAddResource"]
      self.Append:bool = obj["Append"]
      """  Indicates whether to append details or not  """  
      self.AppendedOprSeq:int = obj["AppendedOprSeq"]
      """  Holds new Seq for search of QuoteMtl.RelatedOperation  """  
      self.FinalOperation:bool = obj["FinalOperation"]
      self.AutoReceive:bool = obj["AutoReceive"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  ResourceGrpID  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Job Oper Alternate Method.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteAsmInsp record within the QuoteNum/QuoteLine/AssemblySeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production Quantity required for this assembly per one of it's Parent Part.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for this assembly. Use the Part.IUM as a default.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  """  
      self.Child:int = obj["Child"]
      """  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  QutoeAsm.PartNum of the Parent Assembly  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  QuoteAsm.RevisionNum of the Parent Assembly  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  QuoteAsm.Description of Parent assmebly  """  
      self.ProcessingDetails:bool = obj["ProcessingDetails"]
      """  Boolean to indicate GetDetails has started  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  Clone of the Parent field (.Net keyword issue)  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  Clone of the Child field (.Net keyword issue)  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  Add assembly as "Sub"assembly or "Asm"bly  """  
      self.OverrideNextAsmSeq:bool = obj["OverrideNextAsmSeq"]
      """  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmListTableset:
   def __init__(self, obj):
      self.QuoteAsmList:list[Erp_Tablesets_QuoteAsmListRow] = obj["QuoteAsmList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteAsmRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production Quantity required for this assembly per one of it's Parent Part.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for this assembly. Use the Part.IUM as a default.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  """  
      self.Child:int = obj["Child"]
      """  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  Clone of the Child field (.Net keyword issue)  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.OverrideNextAsmSeq:bool = obj["OverrideNextAsmSeq"]
      """  If this field is true, then the current value of ttQuoteAsm.AssemblySeq will be used when creating new QuoteAsm records. This allows processes, like PLM, to create new QuoteAsm records with a specific AssemblySeq.  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  Clone of the Parent field (.Net keyword issue)  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  QuoteAsm.Description of Parent assmebly  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  QutoeAsm.PartNum of the Parent Assembly  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  QuoteAsm.RevisionNum of the Parent Assembly  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part  """  
      self.ProcessingDetails:bool = obj["ProcessingDetails"]
      """  Boolean to indicate GetDetails has started  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assemblies. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assemblie. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  Add assembly as "Sub"assembly or "Asm"bly  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineSmartString:str = obj["QuoteLineSmartString"]
      self.QuoteLineGroupSeq:int = obj["QuoteLineGroupSeq"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteLineSysRowID:str = obj["QuoteLineSysRowID"]
      self.QuoteLineSmartStringProcessed:bool = obj["QuoteLineSmartStringProcessed"]
      self.QuoteLineReadyToQuote:bool = obj["QuoteLineReadyToQuote"]
      self.QuoteLineContractID:str = obj["QuoteLineContractID"]
      self.QuoteLineKitFlag:str = obj["QuoteLineKitFlag"]
      self.QuoteLineExternalMES:bool = obj["QuoteLineExternalMES"]
      self.QuoteNumQuoted:bool = obj["QuoteNumQuoted"]
      self.QuoteNumQuoteClosed:bool = obj["QuoteNumQuoteClosed"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.QuoteNumCustNum:int = obj["QuoteNumCustNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteAsmTableset:
   def __init__(self, obj):
      self.QuoteAsm:list[Erp_Tablesets_QuoteAsmRow] = obj["QuoteAsm"]
      self.QuoteAsmAttch:list[Erp_Tablesets_QuoteAsmAttchRow] = obj["QuoteAsmAttch"]
      self.QuoteAsmInsp:list[Erp_Tablesets_QuoteAsmInspRow] = obj["QuoteAsmInsp"]
      self.QuoteMtl:list[Erp_Tablesets_QuoteMtlRow] = obj["QuoteMtl"]
      self.QuoteMtlAttch:list[Erp_Tablesets_QuoteMtlAttchRow] = obj["QuoteMtlAttch"]
      self.QuoteMtlInsp:list[Erp_Tablesets_QuoteMtlInspRow] = obj["QuoteMtlInsp"]
      self.QuoteMtlRefDes:list[Erp_Tablesets_QuoteMtlRefDesRow] = obj["QuoteMtlRefDes"]
      self.QuoteOpr:list[Erp_Tablesets_QuoteOprRow] = obj["QuoteOpr"]
      self.QuoteOprAttch:list[Erp_Tablesets_QuoteOprAttchRow] = obj["QuoteOprAttch"]
      self.QuoteOprAction:list[Erp_Tablesets_QuoteOprActionRow] = obj["QuoteOprAction"]
      self.QuoteOprActionParam:list[Erp_Tablesets_QuoteOprActionParamRow] = obj["QuoteOprActionParam"]
      self.QuoteOprInsp:list[Erp_Tablesets_QuoteOprInspRow] = obj["QuoteOprInsp"]
      self.QuoteOpDtl:list[Erp_Tablesets_QuoteOpDtlRow] = obj["QuoteOpDtl"]
      self.QuoteOprMachParam:list[Erp_Tablesets_QuoteOprMachParamRow] = obj["QuoteOprMachParam"]
      self.QuoteAsmRefDes:list[Erp_Tablesets_QuoteAsmRefDesRow] = obj["QuoteAsmRefDes"]
      self.QuoteStage:list[Erp_Tablesets_QuoteStageRow] = obj["QuoteStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteMtlInsp record within the QuoteNum/QuoteLine/AssemblySeq/MtlSeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  """  
      self.Description:str = obj["Description"]
      """  Description of the material. Cannot be blank  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  """  
      self.IUM:str = obj["IUM"]
      """  The issue/usage unit of measure for this material.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvaged material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Quote Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Quote Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.Class:str = obj["Class"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkQty01:int = obj["PBrkQty01"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty02:int = obj["PBrkQty02"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty03:int = obj["PBrkQty03"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty04:int = obj["PBrkQty04"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty05:int = obj["PBrkQty05"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty06:int = obj["PBrkQty06"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty07:int = obj["PBrkQty07"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty08:int = obj["PBrkQty08"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty09:int = obj["PBrkQty09"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty10:int = obj["PBrkQty10"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.PLMMtlSeq:int = obj["PLMMtlSeq"]
      """  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AddrList:str = obj["AddrList"]
      """  Delimited list of Address fields in Company format  """  
      self.AutoSetChkDirect:bool = obj["AutoSetChkDirect"]
      """  This field will tell if the Direct checkbox will be automatically set. If using a NonPartMaster then this field will be set to FALSE. Otherwise if QtyBearing is Yes then this field will be set to TRUE.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  Base Unit of Measure  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This field is used as and internal flag on BO to enable/disable FixedQty column on UI form.  """  
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      """  IsMtlRevisionApproved  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PBImage:str = obj["PBImage"]
      """  Indicates if theres a price break available and if its expired  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDescription:str = obj["RelatedOperationDescription"]
      """  Description from OpMaster of the QuoteOpr.OpCode  """  
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  Salvage Part Base UOM  """  
      self.SalvagePartTrackMulti:bool = obj["SalvagePartTrackMulti"]
      """  Salvage Part Track Dimension Setting  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Scrap Unit of Measure  """  
      self.VendorAddress:str = obj["VendorAddress"]
      """  Vendor address formatted  """  
      self.DispPlanningNumberOfPieces:int = obj["DispPlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.DispSalvagePlanningNumberOfPieces:int = obj["DispSalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvageAttrClassID:str = obj["SalvageAttrClassID"]
      """  ID of related Attribute Class.  """  
      self.SalvageTrackInventoryAttributes:bool = obj["SalvageTrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.SalvageTrackInventoryByRevision:bool = obj["SalvageTrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.   System assigned.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Used to link back to the QuoteLine.   System assigned.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Used to link back to the QuoteAsmbl record.  System assigned.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Used to link back to the QuoteOpr record.  System assigned.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies the QuoteOpDtl.  System assigned.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  The labor rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.OverrideRates:bool = obj["OverrideRates"]
      """  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      self.OperOpStdID:str = obj["OperOpStdID"]
      """  The Operation Standard ID stored in QuoteOpr.  """  
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  Indicates if primary production operation.  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  Indicates if primary setup operation.  """  
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.SubContract:bool = obj["SubContract"]
      """  Flag for sub contract  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter.  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the QuoteOprInsp record within the QuoteNum/QuoteLine/AssemblySeq/OprSeq  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.MachParamSeq:int = obj["MachParamSeq"]
      """  MachParamSeq  """  
      self.RequestCode:str = obj["RequestCode"]
      """  RequestCode  """  
      self.MachineNum:str = obj["MachineNum"]
      """  MachineNum  """  
      self.ToolNum:str = obj["ToolNum"]
      """  ToolNum  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.ParamNum:int = obj["ParamNum"]
      """  ParamNum  """  
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      """  ParamUpperLimit  """  
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      """  ParamNominalValue  """  
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      """  ParamLowerLimit  """  
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      """  ParamDelayValue  """  
      self.SpecEnable:bool = obj["SpecEnable"]
      """  SpecEnable  """  
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      """  SpecControlAlarm  """  
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      """  SpecRunAlarm  """  
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      """  ProcSpecAlarm  """  
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      """  ProcControlAlarm  """  
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      """  PartQualSpecEnable  """  
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      """  PartQualControlEnable  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue Unit of Measure. Applicable only when SubContract = Yes  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description of item to be sent to subcontractor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for quote operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.RunQty:int = obj["RunQty"]
      """  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.StageNumber:str = obj["StageNumber"]
      """  StageNumber  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.AddrList:str = obj["AddrList"]
      """  Vendor Address  """  
      self.APSAltOpDesc:str = obj["APSAltOpDesc"]
      self.APSNextOpDesc:str = obj["APSNextOpDesc"]
      self.APSPrepOpDesc:str = obj["APSPrepOpDesc"]
      self.AutoReceive:bool = obj["AutoReceive"]
      self.DspQtyIUM:str = obj["DspQtyIUM"]
      """  Used to display selected UOM next to unit cost field  """  
      self.EnableAutoRec:bool = obj["EnableAutoRec"]
      """  Indicates whether to enable the AutoReceive field  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  This field is used as a flag to enable/disable the controls binded to SNRequiredOpr column in UI forms.  """  
      self.EnableSNSubConShip:bool = obj["EnableSNSubConShip"]
      """  This field is used as a flag for SNRequiredSubConShip column to determine when to enable/disable it on UI form.  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      self.HoursPerMachine:int = obj["HoursPerMachine"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PBImage:str = obj["PBImage"]
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group Description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.VendorAddress:str = obj["VendorAddress"]
      """  Vendor address formatted  """  
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The Quote Line that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Stage is associated with.  """  
      self.StageSeq:int = obj["StageSeq"]
      """  A sequence number which uniquely identifies stage record within the stage set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.StageNumberDescription:str = obj["StageNumberDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtQuoteAsmTableset:
   def __init__(self, obj):
      self.QuoteAsm:list[Erp_Tablesets_QuoteAsmRow] = obj["QuoteAsm"]
      self.QuoteAsmAttch:list[Erp_Tablesets_QuoteAsmAttchRow] = obj["QuoteAsmAttch"]
      self.QuoteAsmInsp:list[Erp_Tablesets_QuoteAsmInspRow] = obj["QuoteAsmInsp"]
      self.QuoteMtl:list[Erp_Tablesets_QuoteMtlRow] = obj["QuoteMtl"]
      self.QuoteMtlAttch:list[Erp_Tablesets_QuoteMtlAttchRow] = obj["QuoteMtlAttch"]
      self.QuoteMtlInsp:list[Erp_Tablesets_QuoteMtlInspRow] = obj["QuoteMtlInsp"]
      self.QuoteMtlRefDes:list[Erp_Tablesets_QuoteMtlRefDesRow] = obj["QuoteMtlRefDes"]
      self.QuoteOpr:list[Erp_Tablesets_QuoteOprRow] = obj["QuoteOpr"]
      self.QuoteOprAttch:list[Erp_Tablesets_QuoteOprAttchRow] = obj["QuoteOprAttch"]
      self.QuoteOprAction:list[Erp_Tablesets_QuoteOprActionRow] = obj["QuoteOprAction"]
      self.QuoteOprActionParam:list[Erp_Tablesets_QuoteOprActionParamRow] = obj["QuoteOprActionParam"]
      self.QuoteOprInsp:list[Erp_Tablesets_QuoteOprInspRow] = obj["QuoteOprInsp"]
      self.QuoteOpDtl:list[Erp_Tablesets_QuoteOpDtlRow] = obj["QuoteOpDtl"]
      self.QuoteOprMachParam:list[Erp_Tablesets_QuoteOprMachParamRow] = obj["QuoteOprMachParam"]
      self.QuoteAsmRefDes:list[Erp_Tablesets_QuoteAsmRefDesRow] = obj["QuoteAsmRefDes"]
      self.QuoteStage:list[Erp_Tablesets_QuoteStageRow] = obj["QuoteStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindAsm_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipStartAssemblySeq
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      self.ipStartAssemblySeq:int = obj["ipStartAssemblySeq"]
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opAssemblySeq:int = obj["parameters"]
      self.opRowID:str = obj["parameters"]
      pass

      """  output parameters  """  

class FindQuoteMtlByPLMMtlSeq_input:
   """ Required : 
   company
   quoteNum
   quoteLine
   PLMMtlSeq
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.PLMMtlSeq:int = obj["PLMMtlSeq"]
      pass

class FindQuoteMtlByPLMMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.asmSeq:int = obj["parameters"]
      self.mtlSeq:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetAsmOprInfo_input:
   """ Required : 
   ds
   relatedOperation
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.relatedOperation:int = obj["relatedOperation"]
      """  Value of the RelatedOperation that is being tested  """  
      pass

class GetAsmOprInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAsmPartInfo_input:
   """ Required : 
   ds
   defaultRev
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.defaultRev:bool = obj["defaultRev"]
      """  Indicates if the system should try and find the correct RevisionNum
            (yes) or use the value in the dataset (no)  """  
      pass

class GetAsmPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBasePartAndConfigType_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  QuoteDtl sysrowid  """  
      pass

class GetBasePartAndConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBasePartForConfig_input:
   """ Required : 
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      """  QuoteDtl SysRowID  """  
      pass

class GetBasePartForConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDatasetForTreeByRef_input:
   """ Required : 
   ds
   ipQuoteNum
   ipQuoteLine
   ipStartAssemblySeq
   ipCurrentAssemblySeq
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number to return data for.  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number to return data for.  """  
      self.ipStartAssemblySeq:int = obj["ipStartAssemblySeq"]
      """  The Assembly Sequence to return data for.  """  
      self.ipCurrentAssemblySeq:int = obj["ipCurrentAssemblySeq"]
      """  The Assembly Sequence to return data for.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this job number?  """  
      pass

class GetDatasetForTreeByRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDatasetForTreeRefresh_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   assemblySeqList
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number to return data for.  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number to return data for.  """  
      self.assemblySeqList:str = obj["assemblySeqList"]
      """  Tilde separated list of assembly sequences to refresh  """  
      pass

class GetDatasetForTreeRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class GetDatasetForTree_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipStartAssemblySeq
   ipCurrentAssemblySeq
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number to return data for.  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The Quote Line Number to return data for.  """  
      self.ipStartAssemblySeq:int = obj["ipStartAssemblySeq"]
      """  The Assembly Sequence to return data for.  """  
      self.ipCurrentAssemblySeq:int = obj["ipCurrentAssemblySeq"]
      """  The Assembly Sequence to return data for.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this job number?  """  
      pass

class GetDatasetForTree_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class GetDetails_input:
   """ Required : 
   quoteNum
   quoteLine
   targetAsm
   sourceFile
   sourceQuote
   sourceLine
   sourceJob
   sourceAsm
   sourcePart
   sourceRev
   sourceAltMethod
   useMethodForParts
   ipCompleteTree
   getCostsFromTemp
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number of the target Assembly  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line of the target Assembly  """  
      self.targetAsm:int = obj["targetAsm"]
      """  Sequence of the target Assembly  """  
      self.sourceFile:str = obj["sourceFile"]
      """  Source (Quote, Job, or Method) of the details to copy  """  
      self.sourceQuote:int = obj["sourceQuote"]
      """  Quote Number to get details from (populated when sourceFile = "Quote")  """  
      self.sourceLine:int = obj["sourceLine"]
      """  Quote Line to get details from (populated when sourceFile = "Quote")  """  
      self.sourceJob:str = obj["sourceJob"]
      """  Job Number to get details from (populated when sourceFile = "Job")  """  
      self.sourceAsm:int = obj["sourceAsm"]
      """  Quote Assembly to get details from (populated when sourceFile = "Quote" or "Job")  """  
      self.sourcePart:str = obj["sourcePart"]
      """  Part Num to get details from (populated when sourceFile = "Method")  """  
      self.sourceRev:str = obj["sourceRev"]
      """  Revision number to get details from (populated when sourceFile = "Method")  """  
      self.sourceAltMethod:str = obj["sourceAltMethod"]
      """  Alternate Method to get details from (populated when sourceFile = "Method")  """  
      self.useMethodForParts:bool = obj["useMethodForParts"]
      """  If true use the method passed in for all parts in assemblies, if false
            use the assembly part's default method.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      self.getCostsFromTemp:bool = obj["getCostsFromTemp"]
      """  Would you like get an exact copy of materials costs?  """  
      pass

class GetDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.partErrors:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_QuoteAsmListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMtlBuyItInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetMtlBuyItInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMtlConfigPartRevAndConfigType_input:
   """ Required : 
   sysRowID
   revisionNum
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      self.revisionNum:str = obj["revisionNum"]
      pass

class GetMtlConfigPartRevAndConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMtlConfigPartRev_input:
   """ Required : 
   sysRowID
   revisionNum
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      self.revisionNum:str = obj["revisionNum"]
      pass

class GetMtlConfigPartRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cfgPartNum:str = obj["parameters"]
      self.cfgRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMtlDirectInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetMtlDirectInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMtlOprInfo_input:
   """ Required : 
   relatedOperation
   ds
   """  
   def __init__(self, obj):
      self.relatedOperation:int = obj["relatedOperation"]
      """  Value of the RelatedOperation that is being tested  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetMtlOprInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMtlPartInfo_input:
   """ Required : 
   ds
   partName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.partName:str = obj["partName"]
      """  Identifies the PartNum field to validate either PartNum or SalvagePartNum  """  
      pass

class GetMtlPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMtlVendorInfo_input:
   """ Required : 
   ds
   vendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.vendorID:str = obj["vendorID"]
      """  Proposed Vendor ID  """  
      pass

class GetMtlVendorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAssembly_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   bomLevel
   priorAssemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      """  Assembly's parent Quote  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Assembly's parent Quote detail Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly's parent assembly Seq  """  
      self.bomLevel:int = obj["bomLevel"]
      """  Assembly's parent BOMLevel  """  
      self.priorAssemblySeq:int = obj["priorAssemblySeq"]
      """  If adding a sub-assembly record, this value is 0.  If
            inserting after a specific assembly then use that record's assembly seq (must be different
            from the parent assembly seq)  """  
      pass

class GetNewAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOperation_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   subContract
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      """  Operations's parent Quote  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Operations's parent Quote detail Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Operations's parent assembly Seq  """  
      self.subContract:bool = obj["subContract"]
      """  Operations's sub contract type  """  
      pass

class GetNewOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteAsmAttch_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewQuoteAsmAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteAsmInsp_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewQuoteAsmInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteAsmRefDes_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewQuoteAsmRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteAsm_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetNewQuoteAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteMtlAttch_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewQuoteMtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteMtlInsp_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewQuoteMtlInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteMtlRefDes_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewQuoteMtlRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteMtl_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewQuoteMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOpDtl_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewQuoteOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOprActionParam_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   actionSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.actionSeq:int = obj["actionSeq"]
      pass

class GetNewQuoteOprActionParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOprAction_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewQuoteOprAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOprAttch_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewQuoteOprAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOprInsp_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewQuoteOprInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOprMachParam_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewQuoteOprMachParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteOpr_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewQuoteOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteStage_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewQuoteStage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOprOpCodeInfo_input:
   """ Required : 
   ProposedOpCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedOpCode:str = obj["ProposedOpCode"]
      """  The proposed Operation Code  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetOprOpCodeInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RefreshMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOprOpStdInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetOprOpStdInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOprPartInfo_input:
   """ Required : 
   ds
   partName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.partName:str = obj["partName"]
      """  Identifies the PartNum field to validate either PartNum or SalvagePartNum  """  
      pass

class GetOprPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOprStdFormatInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetOprStdFormatInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetProjectRoles_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetQuoteEngUIDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultValues:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetQuoteMtlIsMtlConfigurationOn_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class GetQuoteMtlIsMtlConfigurationOn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuoteAsm
   whereClauseQuoteAsmAttch
   whereClauseQuoteAsmInsp
   whereClauseQuoteMtl
   whereClauseQuoteMtlAttch
   whereClauseQuoteMtlInsp
   whereClauseQuoteMtlRefDes
   whereClauseQuoteOpr
   whereClauseQuoteOprAttch
   whereClauseQuoteOprAction
   whereClauseQuoteOprActionParam
   whereClauseQuoteOprInsp
   whereClauseQuoteOpDtl
   whereClauseQuoteOprMachParam
   whereClauseQuoteAsmRefDes
   whereClauseQuoteStage
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteAsm:str = obj["whereClauseQuoteAsm"]
      self.whereClauseQuoteAsmAttch:str = obj["whereClauseQuoteAsmAttch"]
      self.whereClauseQuoteAsmInsp:str = obj["whereClauseQuoteAsmInsp"]
      self.whereClauseQuoteMtl:str = obj["whereClauseQuoteMtl"]
      self.whereClauseQuoteMtlAttch:str = obj["whereClauseQuoteMtlAttch"]
      self.whereClauseQuoteMtlInsp:str = obj["whereClauseQuoteMtlInsp"]
      self.whereClauseQuoteMtlRefDes:str = obj["whereClauseQuoteMtlRefDes"]
      self.whereClauseQuoteOpr:str = obj["whereClauseQuoteOpr"]
      self.whereClauseQuoteOprAttch:str = obj["whereClauseQuoteOprAttch"]
      self.whereClauseQuoteOprAction:str = obj["whereClauseQuoteOprAction"]
      self.whereClauseQuoteOprActionParam:str = obj["whereClauseQuoteOprActionParam"]
      self.whereClauseQuoteOprInsp:str = obj["whereClauseQuoteOprInsp"]
      self.whereClauseQuoteOpDtl:str = obj["whereClauseQuoteOpDtl"]
      self.whereClauseQuoteOprMachParam:str = obj["whereClauseQuoteOprMachParam"]
      self.whereClauseQuoteAsmRefDes:str = obj["whereClauseQuoteAsmRefDes"]
      self.whereClauseQuoteStage:str = obj["whereClauseQuoteStage"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
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

class InsertBOMAsm_input:
   """ Required : 
   ipParentQuoteAsmRowid
   ipSourceRowid
   ipOperSeq
   ipDroppedAs
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipParentQuoteAsmRowid:str = obj["ipParentQuoteAsmRowid"]
      """  The rowid of the parent quoteasm to add to  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be jobasmbl or quoteasm to be added to the parent quoteasm  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what. valid values: JobAsmbl, JobAsmbl-AsMtl, QuoteAsm, QuoteAsm-AsMtl  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertBOMAsm_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertBOMMtl_input:
   """ Required : 
   ipParentQuoteAsmRowid
   ipSourceRowid
   ipOperSeq
   ipMtlSeq
   ipBeforeMtlRowid
   ipDroppedAs
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipParentQuoteAsmRowid:str = obj["ipParentQuoteAsmRowid"]
      """  The rowid of the quoteasm record to add the material to  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be partmtl, jobmtl, or
            quotemtl to be added to the parent quoteasm  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The material seq to use  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert material before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
            valid values: PartMtl, PartMtl-AsAsm, JobMtl-AsAsm, JobMtl, QuoteMtl-AsAsm, QuoteMtl  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertBOMMtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertBOMOper_input:
   """ Required : 
   ipParentQuoteAsmRowid
   ipSourceRowid
   ipNewOperSeq
   ipBeforeOperRowid
   ipDroppedAs
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipParentQuoteAsmRowid:str = obj["ipParentQuoteAsmRowid"]
      """  The rowid of the parent jobasmbl to add to  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be joboper, partopr, or
            quoteopr to be added to the parent jobasmbl  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
            valid values: PartOpr, JobOper, QuoteOpr  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertBOMOper_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertMaterial_input:
   """ Required : 
   ipQuoteAsmRowID
   ipPartNum
   ipOperSeq
   ipMtlSeq
   ipBeforeMtlRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the material to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The part number being added  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The material seq to use  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert material before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertMaterial_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertNewSubAssembly_input:
   """ Required : 
   ipQuoteAsmRowID
   ipPartNum
   ipOperSeq
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the material to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The part number being added  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertNewSubAssembly_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.revisionNum:str = obj["parameters"]
      self.newQuoteAsmSeq:int = obj["parameters"]
      self.newQuoteAsmSysRowID:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOpDtlCapability_input:
   """ Required : 
   ipQuoteOprRowID
   ipCapabilityID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteOprRowID:str = obj["ipQuoteOprRowID"]
      """  The rowid of the QuoteOpr record to add the operation detail to  """  
      self.ipCapabilityID:str = obj["ipCapabilityID"]
      """  The Capability ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOpDtlCapability_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertOpDtlResourceGrp_input:
   """ Required : 
   ipQuoteOprRowID
   ipResourceGrpID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteOprRowID:str = obj["ipQuoteOprRowID"]
      """  The rowid of the QuoteOpr record to add the operation detail to  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The Resource Group ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOpDtlResourceGrp_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertOpDtlResource_input:
   """ Required : 
   ipQuoteOprRowID
   ipResourceID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteOprRowID:str = obj["ipQuoteOprRowID"]
      """  The rowid of the QuoteOpr record to add the operation detail to  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The Resource ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOpDtlResource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class InsertOperCapability_input:
   """ Required : 
   ipQuoteAsmRowID
   ipCapabilityID
   ipNewOprSeq
   ipBeforeOprRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the operation detail to  """  
      self.ipCapabilityID:str = obj["ipCapabilityID"]
      """  The Capability ID being added  """  
      self.ipNewOprSeq:int = obj["ipNewOprSeq"]
      """  The new operation seq  """  
      self.ipBeforeOprRowid:str = obj["ipBeforeOprRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOperCapability_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOperResGroup_input:
   """ Required : 
   ipQuoteAsmRowID
   ipResourceGrpID
   ipNewOprSeq
   ipBeforeOprRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the operation detail to  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The Resource Group ID being added  """  
      self.ipNewOprSeq:int = obj["ipNewOprSeq"]
      """  The new operation seq  """  
      self.ipBeforeOprRowid:str = obj["ipBeforeOprRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOperResGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOperResource_input:
   """ Required : 
   ipQuoteAsmRowID
   ipResourceID
   ipNewOprSeq
   ipBeforeOprRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the operation detail to  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The Resource ID being added  """  
      self.ipNewOprSeq:int = obj["ipNewOprSeq"]
      """  The new operation seq  """  
      self.ipBeforeOprRowid:str = obj["ipBeforeOprRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOperResource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOperationOP_input:
   """ Required : 
   ipQuoteAsmRowID
   ipOpCode
   ipNewOprSeq
   ipBeforeOperRowid
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the operation to  """  
      self.ipOpCode:str = obj["ipOpCode"]
      """  The operation code being added  """  
      self.ipNewOprSeq:int = obj["ipNewOprSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertOperationOP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertSubAssembly_input:
   """ Required : 
   ipQuoteAsmRowID
   ipPartNum
   ipOperSeq
   ipReturn
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipQuoteAsmRowID:str = obj["ipQuoteAsmRowID"]
      """  The rowid of the QuoteAsm record to add the material to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The part number being added  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class InsertSubAssembly_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class JobPartBeforeGetNew_output:
   def __init__(self, obj):
      pass

class OnChangingAttributeSetQuoteAsm_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingAttributeSetQuoteAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSetQuoteMtl_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingAttributeSetQuoteMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSetQuoteOpr_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingAttributeSetQuoteOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMtlRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingMtlRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPiecesQuoteMtl_input:
   """ Required : 
   relatedColumn
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.relatedColumn:str = obj["relatedColumn"]
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingNumberOfPiecesQuoteMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPiecesQuoteOpr_input:
   """ Required : 
   relatedColumn
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.relatedColumn:str = obj["relatedColumn"]
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingNumberOfPiecesQuoteOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingQuoteOprRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingQuoteOprRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSalvageRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class OnChangingSalvageRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreGetDetails_input:
   """ Required : 
   sourcePartNum
   sourceRevisionNum
   sourceFile
   targetJobNum
   targetAsm
   sourceSysRowID
   """  
   def __init__(self, obj):
      self.sourcePartNum:str = obj["sourcePartNum"]
      """  Indicates the source part number to get details from  """  
      self.sourceRevisionNum:str = obj["sourceRevisionNum"]
      """  Indicates the source revision number to get details from  """  
      self.sourceFile:str = obj["sourceFile"]
      """  Indicates where the details are being appended from.  Either Quote,
            Job or Method  """  
      self.targetJobNum:str = obj["targetJobNum"]
      """  Target Job Number  """  
      self.targetAsm:int = obj["targetAsm"]
      """  Sequence of the target Assembly  """  
      self.sourceSysRowID:str = obj["sourceSysRowID"]
      pass

class PreGetDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.BasePartNum:str = obj["parameters"]
      self.BaseRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class QuoteAsmChildDelete_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class QuoteAsmChildDelete_output:
   def __init__(self, obj):
      pass

class QuoteOprInitSNReqSubCon_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class QuoteOprInitSNReqSubCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshMtlPriceBreak_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   mtlSeq
   vendorNum
   pum
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      """  Material Quote  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Material Quote Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Material Assembly  """  
      self.mtlSeq:int = obj["mtlSeq"]
      """  Material Sequence  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number from vendor price break  """  
      self.pum:str = obj["pum"]
      """  Purchasing Unit of measure for the Part  """  
      self.effectiveDate:str = obj["effectiveDate"]
      """  Effective date from vendor price break  """  
      pass

class RefreshMtlPriceBreak_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshOprPriceBreak_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   assemblySeq
   oprSeq
   vendorNum
   pum
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      """  Operation Quote  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Operation Quote Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Operation Assembly  """  
      self.oprSeq:int = obj["oprSeq"]
      """  Operation Sequence  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number from vendor price break  """  
      self.pum:str = obj["pum"]
      self.effectiveDate:str = obj["effectiveDate"]
      """  Effective date from vendor price break  """  
      pass

class RefreshOprPriceBreak_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResequenceMaterial_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   reseqOption
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly Sequences  """  
      self.reseqOption:str = obj["reseqOption"]
      """  "M" for Material, "P" for Part, or "B" for Bubble  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class ResequenceMaterial_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class ResequenceOperations_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly Sequence  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to return a complete dataset for this QuoteAsm?  """  
      pass

class ResequenceOperations_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteAsmTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuoteAsmTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuoteAsmTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateInspection_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   iptable
   setRev
   ds
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed SpecID value  """  
      self.iptable:str = obj["iptable"]
      """  table name  """  
      self.setRev:bool = obj["setRev"]
      """  if set default revision  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ValidateInspection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLinkToContractData_input:
   """ Required : 
   bLinkToContract
   iQuoteNum
   iQuoteLine
   sPartNum
   sTablename
   """  
   def __init__(self, obj):
      self.bLinkToContract:bool = obj["bLinkToContract"]
      self.iQuoteNum:int = obj["iQuoteNum"]
      self.iQuoteLine:int = obj["iQuoteLine"]
      self.sPartNum:str = obj["sPartNum"]
      self.sTablename:str = obj["sTablename"]
      pass

class ValidateLinkToContractData_output:
   def __init__(self, obj):
      pass

class ValidatePartToLinkToContract_input:
   """ Required : 
   bLinkToContract
   iQuoteNum
   iQuoteLine
   partNum
   tableName
   """  
   def __init__(self, obj):
      self.bLinkToContract:bool = obj["bLinkToContract"]
      self.iQuoteNum:int = obj["iQuoteNum"]
      self.iQuoteLine:int = obj["iQuoteLine"]
      self.partNum:str = obj["partNum"]
      self.tableName:str = obj["tableName"]
      pass

class ValidatePartToLinkToContract_output:
   def __init__(self, obj):
      pass

class ValidateSNReqValues_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipQuoteAsmSeq
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  Quote Number  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  Quote Line  """  
      self.ipQuoteAsmSeq:int = obj["ipQuoteAsmSeq"]
      """  Assembly Seq  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

class ValidateSNReqValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteAsmTableset] = obj["ds"]
      pass

      """  output parameters  """  

class checkQuotePartConfiguration_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number for which we are checking  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote number Line for which we are checking  """  
      pass

class checkQuotePartConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.canGetDetails:bool = obj["canGetDetails"]
      self.needsConfiguration:bool = obj["needsConfiguration"]
      self.isNIC:bool = obj["isNIC"]
      self.reasonMessage:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      self.targetSysRowID:str = obj["parameters"]
      self.partNum:str = obj["parameters"]
      self.revisionNum:str = obj["parameters"]
      self.kitFlag:str = obj["parameters"]
      self.kitsLoaded:bool = obj["kitsLoaded"]
      self.smartStringProcessed:bool = obj["smartStringProcessed"]
      self.smartString:str = obj["parameters"]
      pass

      """  output parameters  """  

