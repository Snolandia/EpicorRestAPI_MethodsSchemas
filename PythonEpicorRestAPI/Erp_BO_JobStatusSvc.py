import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobStatusSvc
# Description: The JobStatus main object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JobStatus(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobStatus
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus",headers=creds) as resp:
           return await resp.json()

async def post_JobStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobStatus_Company_JobNum(Company, JobNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobStatu item
   Description: Calls GetByID to retrieve the JobStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobStatus_Company_JobNum(Company, JobNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobStatu for the service
   Description: Calls UpdateExt to update JobStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobStatus_Company_JobNum(Company, JobNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobStatu item
   Description: Call UpdateExt to delete JobStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_JobStatus_Company_JobNum_JobAsmbls(Company, JobNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JobAsmbls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JobAsmbls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobAsmbls",headers=creds) as resp:
           return await resp.json()

async def get_JobStatus_Company_JobNum_JobAsmbls_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobAsmbl item
   Description: Calls GetByID to retrieve the JobAsmbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmbl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_JobStatus_Company_JobNum_JobMtls(Company, JobNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JobMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JobMtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobMtls",headers=creds) as resp:
           return await resp.json()

async def get_JobStatus_Company_JobNum_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobMtl item
   Description: Calls GetByID to retrieve the JobMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_JobAsmbls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobAsmbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobAsmbls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls",headers=creds) as resp:
           return await resp.json()

async def post_JobAsmbls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobAsmbls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobAsmbls_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobAsmbl item
   Description: Calls GetByID to retrieve the JobAsmbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobAsmbls_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobAsmbl for the service
   Description: Calls UpdateExt to update JobAsmbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobAsmbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobAsmbls_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobAsmbl item
   Description: Call UpdateExt to delete JobAsmbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobAsmbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_JobMtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobMtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls",headers=creds) as resp:
           return await resp.json()

async def post_JobMtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobMtl item
   Description: Calls GetByID to retrieve the JobMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobMtl for the service
   Description: Calls UpdateExt to update JobMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobMtl item
   Description: Call UpdateExt to delete JobMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobHead, whereClauseJobAsmbl, whereClauseJobMtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobHead=" + whereClauseJobHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJobMtl=" + whereClauseJobMtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "jobNum=" + jobNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AutoAllocateJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoAllocateJobMtl
   Description: This method allocates any selected job materials
   OperationID: AutoAllocateJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoAllocateJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocateJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoReserveJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoReserveJobMtl
   Description: This method reserves any selected job materials
   OperationID: AutoReserveJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserveJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobHeadFirm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobHeadFirm
   Description: This method validates the JobHead.JobFirm and potentially changes the jobreleased
fields.
This method should run when the JobHead.JobFirm field changes.
   OperationID: ChangeJobHeadFirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobHeadJobEngineered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobHeadJobEngineered
   Description: This method validates the JobHead.JobEngineered and potentially changes the jobreleased field.
This method should run when the JobHead.JobEngineered field changes.
   OperationID: ChangeJobHeadJobEngineered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadJobEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadJobEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobHeadJobReleased(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobHeadJobReleased
   Description: This method validates the JobHead.JobReleased and potentially changes the jobengineered
and/or jobfirm fields.
This method should run when the JobHead.JobReleased field changes.
   OperationID: ChangeJobHeadJobReleased
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadJobReleased_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadJobReleased_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDJobMtl
   Description: Performs the standard GetByID and includes any related job materials
   OperationID: GetByIDJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the JobHeadSearch records which will be a subset
of the JobHead records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the JobHeadSearch records which will be a subset
of the JobHead records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassUpdate
   Description: Call this method to update multiple JobHead records.
   OperationID: MassUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobAsmbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobAsmbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobAsmbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobAsmblRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobMtlRow] = obj["value"]
      pass

class Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  Reassign Serial Numbers Assembly  """  
      self.TLAODCCost:int = obj["TLAODCCost"]
      """  This Level Actual Other Direct Cost.  """  
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      """  AssemblyMatch  """  
      self.JdfStatus:str = obj["JdfStatus"]
      """  JdfStatus  """  
      self.PressDevice:str = obj["PressDevice"]
      """  PressDevice  """  
      self.DigitalFileName:str = obj["DigitalFileName"]
      """  DigitalFileName  """  
      self.PrepressJobName:str = obj["PrepressJobName"]
      """  PrepressJobName  """  
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      """  JdfPrepressAction  """  
      self.SendToPress:bool = obj["SendToPress"]
      """  SendToPress  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      """  SendToPressInitiator  """  
      self.OperationType:int = obj["OperationType"]
      """  OperationType  """  
      self.SendToPrePress:bool = obj["SendToPrePress"]
      """  SendToPrePress  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      """  PartPlanInfo  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ShowWarningBOMResequence:bool = obj["ShowWarningBOMResequence"]
      """  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.TLATotalCost:int = obj["TLATotalCost"]
      """  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  """  
      self.TLETotalCost:int = obj["TLETotalCost"]
      """  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.SOExists:bool = obj["SOExists"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Part Description  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Track Dimension  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Track Lots  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Track Serial Num  """  
      self.EquipOEM:str = obj["EquipOEM"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.EquipDescription:str = obj["EquipDescription"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttrDescription:str = obj["AttrDescription"]
      """  Description of values in set  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
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
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
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
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
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
      self.RelatedStage:str = obj["RelatedStage"]
      """  The identification of related StageNo.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the job material should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job material is ready to be fulfilled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      """  The display of extended price.  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  The display unit price.  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display extended price  """  
      self.dspBuyIt:bool = obj["dspBuyIt"]
      """  BuyIt field for display in the UI.  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM (readonly)  """  
      self.EnableBackflush:bool = obj["EnableBackflush"]
      """  Should the backflush field be enabled?  """  
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      """  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  """  
      self.EnableConfigure:bool = obj["EnableConfigure"]
      """  flag to determine whether the Configure Option should be enabled.  """  
      self.EnableDirect:bool = obj["EnableDirect"]
      """  flag to determine whether the Make Direct field should be enabled.  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      """  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EstCost:int = obj["EstCost"]
      """  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  """  
      self.IPCaller:str = obj["IPCaller"]
      """  The name of the calling program  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      """  IsMtlRevisionApproved  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PlantList:str = obj["PlantList"]
      """  Calculated field gets list of available Sites  """  
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      """  Price Per Code Description  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  The description of the related operation  """  
      self.RetainValues:bool = obj["RetainValues"]
      """  Logical used to determine if record is created from PO Entry.  """  
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  BaseUOM for SalvagePartNum  """  
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      """  Satatus of InspectionRequired image on JobMaterial form.  """  
      self.SubContract:bool = obj["SubContract"]
      """  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  """  
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      """  Can the backflush be unchecked?  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.EnableSalvageAttributeSetSearch:bool = obj["EnableSalvageAttributeSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SkipUnitPriceCalc:bool = obj["SkipUnitPriceCalc"]
      """  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this job material is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      """  Indicates this row is selected for action.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  The allocated quantity for this job material.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  The reserved quantity for this job material.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  The available quantity for this job material.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqPartNum:str = obj["AssemblySeqPartNum"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.JobNumPartNum:str = obj["JobNumPartNum"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PlantName:str = obj["PlantName"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.PurMiscCodeDescription:str = obj["PurMiscCodeDescription"]
      self.PurMiscCodeLCAmount:int = obj["PurMiscCodeLCAmount"]
      self.PurMiscCodeLCDisburseMethod:str = obj["PurMiscCodeLCDisburseMethod"]
      self.PurMiscCodeLCCurrencyCode:str = obj["PurMiscCodeLCCurrencyCode"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SalvageAttributeSetIDDescription:str = obj["SalvageAttributeSetIDDescription"]
      self.SalvageAttributeSetIDShortDescription:str = obj["SalvageAttributeSetIDShortDescription"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumTrackInventoryByRevision:bool = obj["SalvagePartNumTrackInventoryByRevision"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SCMiscCodeDescription:str = obj["SCMiscCodeDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AutoAllocateJobMtl_input:
   """ Required : 
   jobStatusTableset
   jobNum
   """  
   def __init__(self, obj):
      self.jobStatusTableset:list[Erp_Tablesets_JobStatusTableset] = obj["jobStatusTableset"]
      self.jobNum:str = obj["jobNum"]
      """  The Job Number  """  
      pass

class AutoAllocateJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.jobStatusTableset:list[Erp_Tablesets_JobStatusTableset] = obj["jobStatusTableset"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class AutoReserveJobMtl_input:
   """ Required : 
   jobStatusTableset
   jobNum
   """  
   def __init__(self, obj):
      self.jobStatusTableset:list[Erp_Tablesets_JobStatusTableset] = obj["jobStatusTableset"]
      self.jobNum:str = obj["jobNum"]
      """  The Job Number  """  
      pass

class AutoReserveJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.jobStatusTableset:list[Erp_Tablesets_JobStatusTableset] = obj["jobStatusTableset"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeJobHeadFirm_input:
   """ Required : 
   ipProposedJobFirm
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedJobFirm:bool = obj["ipProposedJobFirm"]
      """  The new proposed JobFirm value  """  
      self.jobNum:str = obj["jobNum"]
      """  The job number to search appropriate record  """  
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class ChangeJobHeadFirm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobHeadJobEngineered_input:
   """ Required : 
   ipProposedJobEngineered
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedJobEngineered:bool = obj["ipProposedJobEngineered"]
      """  The new proposed JobEngineered value  """  
      self.jobNum:str = obj["jobNum"]
      """  The job number to search appropriate record  """  
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class ChangeJobHeadJobEngineered_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobHeadJobReleased_input:
   """ Required : 
   ipProposedJobReleased
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedJobReleased:bool = obj["ipProposedJobReleased"]
      """  The new proposed JobReleased value  """  
      self.jobNum:str = obj["jobNum"]
      """  The job number to search appropriate record  """  
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class ChangeJobHeadJobReleased_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  Reassign Serial Numbers Assembly  """  
      self.TLAODCCost:int = obj["TLAODCCost"]
      """  This Level Actual Other Direct Cost.  """  
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      """  AssemblyMatch  """  
      self.JdfStatus:str = obj["JdfStatus"]
      """  JdfStatus  """  
      self.PressDevice:str = obj["PressDevice"]
      """  PressDevice  """  
      self.DigitalFileName:str = obj["DigitalFileName"]
      """  DigitalFileName  """  
      self.PrepressJobName:str = obj["PrepressJobName"]
      """  PrepressJobName  """  
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      """  JdfPrepressAction  """  
      self.SendToPress:bool = obj["SendToPress"]
      """  SendToPress  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      """  SendToPressInitiator  """  
      self.OperationType:int = obj["OperationType"]
      """  OperationType  """  
      self.SendToPrePress:bool = obj["SendToPrePress"]
      """  SendToPrePress  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      """  PartPlanInfo  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ShowWarningBOMResequence:bool = obj["ShowWarningBOMResequence"]
      """  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.TLATotalCost:int = obj["TLATotalCost"]
      """  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  """  
      self.TLETotalCost:int = obj["TLETotalCost"]
      """  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.SOExists:bool = obj["SOExists"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Part Description  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Track Dimension  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Track Lots  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Track Serial Num  """  
      self.EquipOEM:str = obj["EquipOEM"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.EquipDescription:str = obj["EquipDescription"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttrDescription:str = obj["AttrDescription"]
      """  Description of values in set  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadListTableset:
   def __init__(self, obj):
      self.JobHeadList:list[Erp_Tablesets_JobHeadListRow] = obj["JobHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
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
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
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
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
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
      self.RelatedStage:str = obj["RelatedStage"]
      """  The identification of related StageNo.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the job material should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job material is ready to be fulfilled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      """  The display of extended price.  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  The display unit price.  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display extended price  """  
      self.dspBuyIt:bool = obj["dspBuyIt"]
      """  BuyIt field for display in the UI.  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM (readonly)  """  
      self.EnableBackflush:bool = obj["EnableBackflush"]
      """  Should the backflush field be enabled?  """  
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      """  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  """  
      self.EnableConfigure:bool = obj["EnableConfigure"]
      """  flag to determine whether the Configure Option should be enabled.  """  
      self.EnableDirect:bool = obj["EnableDirect"]
      """  flag to determine whether the Make Direct field should be enabled.  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      """  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EstCost:int = obj["EstCost"]
      """  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  """  
      self.IPCaller:str = obj["IPCaller"]
      """  The name of the calling program  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      """  IsMtlRevisionApproved  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PlantList:str = obj["PlantList"]
      """  Calculated field gets list of available Sites  """  
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      """  Price Per Code Description  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  The description of the related operation  """  
      self.RetainValues:bool = obj["RetainValues"]
      """  Logical used to determine if record is created from PO Entry.  """  
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  BaseUOM for SalvagePartNum  """  
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      """  Satatus of InspectionRequired image on JobMaterial form.  """  
      self.SubContract:bool = obj["SubContract"]
      """  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  """  
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      """  Can the backflush be unchecked?  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.EnableSalvageAttributeSetSearch:bool = obj["EnableSalvageAttributeSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SkipUnitPriceCalc:bool = obj["SkipUnitPriceCalc"]
      """  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this job material is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      """  Indicates this row is selected for action.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  The allocated quantity for this job material.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  The reserved quantity for this job material.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  The available quantity for this job material.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqPartNum:str = obj["AssemblySeqPartNum"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.JobNumPartNum:str = obj["JobNumPartNum"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PlantName:str = obj["PlantName"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.PurMiscCodeDescription:str = obj["PurMiscCodeDescription"]
      self.PurMiscCodeLCAmount:int = obj["PurMiscCodeLCAmount"]
      self.PurMiscCodeLCDisburseMethod:str = obj["PurMiscCodeLCDisburseMethod"]
      self.PurMiscCodeLCCurrencyCode:str = obj["PurMiscCodeLCCurrencyCode"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SalvageAttributeSetIDDescription:str = obj["SalvageAttributeSetIDDescription"]
      self.SalvageAttributeSetIDShortDescription:str = obj["SalvageAttributeSetIDShortDescription"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumTrackInventoryByRevision:bool = obj["SalvagePartNumTrackInventoryByRevision"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SCMiscCodeDescription:str = obj["SCMiscCodeDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobStatusTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.JobAsmbl:list[Erp_Tablesets_JobAsmblRow] = obj["JobAsmbl"]
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJobStatusTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.JobAsmbl:list[Erp_Tablesets_JobAsmblRow] = obj["JobAsmbl"]
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDJobMtl_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      pass

class GetByIDJobMtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobStatusTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobStatusTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobStatusTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobStatusTableset] = obj["returnObj"]
      pass

class GetListFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobHeadListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobHeadListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_JobHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobAsmbl_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      pass

class GetNewJobAsmbl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJobHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class GetNewJobHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobHead
   whereClauseJobAsmbl
   whereClauseJobMtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      self.whereClauseJobAsmbl:str = obj["whereClauseJobAsmbl"]
      self.whereClauseJobMtl:str = obj["whereClauseJobMtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobStatusTableset] = obj["returnObj"]
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

class MassUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class MassUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobStatusTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobStatusTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobStatusTableset] = obj["ds"]
      pass

      """  output parameters  """  

