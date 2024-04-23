import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CourseSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Courses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Courses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Courses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses",headers=creds) as resp:
           return await resp.json()

async def post_Courses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Courses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Courses_Company_CourseID(Company, CourseID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Course item
   Description: Calls GetByID to retrieve the Course item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Course
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses(" + Company + "," + CourseID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Courses_Company_CourseID(Company, CourseID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Course for the service
   Description: Calls UpdateExt to update Course. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Course
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses(" + Company + "," + CourseID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Courses_Company_CourseID(Company, CourseID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Course item
   Description: Call UpdateExt to delete Course item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Course
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses(" + Company + "," + CourseID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Courses_Company_CourseID_CourseRevisions(Company, CourseID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CourseRevisions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseRevisions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses(" + Company + "," + CourseID + ")/CourseRevisions",headers=creds) as resp:
           return await resp.json()

async def get_Courses_Company_CourseID_CourseRevisions_Company_CourseID_RevisionCode(Company, CourseID, RevisionCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseRevision item
   Description: Calls GetByID to retrieve the CourseRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseRevision1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/Courses(" + Company + "," + CourseID + ")/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CourseRevisions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseRevisions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions",headers=creds) as resp:
           return await resp.json()

async def post_CourseRevisions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseRevisionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseRevisionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisions_Company_CourseID_RevisionCode(Company, CourseID, RevisionCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseRevision item
   Description: Calls GetByID to retrieve the CourseRevision item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseRevisionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CourseRevisions_Company_CourseID_RevisionCode(Company, CourseID, RevisionCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CourseRevision for the service
   Description: Calls UpdateExt to update CourseRevision. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseRevisionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CourseRevisions_Company_CourseID_RevisionCode(Company, CourseID, RevisionCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CourseRevision item
   Description: Call UpdateExt to delete CourseRevision item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseRevision
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisions_Company_CourseID_RevisionCode_CourseRevisionAttches(Company, CourseID, RevisionCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CourseRevisionAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseRevisionAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseRevisionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")/CourseRevisionAttches",headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisions_Company_CourseID_RevisionCode_CourseRevisionAttches_Company_CourseID_RevisionCode_DrawingSeq(Company, CourseID, RevisionCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseRevisionAttch item
   Description: Calls GetByID to retrieve the CourseRevisionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseRevisionAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseRevisionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisions(" + Company + "," + CourseID + "," + RevisionCode + ")/CourseRevisionAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisionAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CourseRevisionAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseRevisionAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseRevisionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisionAttches",headers=creds) as resp:
           return await resp.json()

async def post_CourseRevisionAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseRevisionAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseRevisionAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseRevisionAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisionAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CourseRevisionAttches_Company_CourseID_RevisionCode_DrawingSeq(Company, CourseID, RevisionCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CourseRevisionAttch item
   Description: Calls GetByID to retrieve the CourseRevisionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseRevisionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseRevisionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisionAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CourseRevisionAttches_Company_CourseID_RevisionCode_DrawingSeq(Company, CourseID, RevisionCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CourseRevisionAttch for the service
   Description: Calls UpdateExt to update CourseRevisionAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseRevisionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseRevisionAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisionAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CourseRevisionAttches_Company_CourseID_RevisionCode_DrawingSeq(Company, CourseID, RevisionCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CourseRevisionAttch item
   Description: Call UpdateExt to delete CourseRevisionAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseRevisionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CourseID: Desc: CourseID   Required: True   Allow empty value : True
      :param RevisionCode: Desc: RevisionCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/CourseRevisionAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCourse, whereClauseCourseRevision, whereClauseCourseRevisionAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCourse=" + whereClauseCourse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCourseRevision=" + whereClauseCourseRevision
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCourseRevisionAttch=" + whereClauseCourseRevisionAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(courseID, epicorHeaders = None):
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
   params += "courseID=" + courseID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateCourse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateCourse
   OperationID: DuplicateCourse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateCourse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateCourse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCourseDurationTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCourseDurationTypeList
   OperationID: GetCourseDurationTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCourseDurationTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCourseExpirationTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCourseExpirationTypeList
   Description: ///  This method returns the list of Expiration type codes and descriptions .  ///
   OperationID: GetCourseExpirationTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCourseExpirationTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateCourseDeletion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCourseDeletion
   Description: Method to validate the possibility of Course deletion.
   OperationID: ValidateCourseDeletion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCourseDeletion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCourseDeletion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCourseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCourseID
   Description: Validation of course ID
   OperationID: ValidateCourseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCourseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCourseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCourseRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCourseRevision
   Description: Validation of course revision
   OperationID: ValidateCourseRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCourseRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCourseRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCourseRevisionDeletion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCourseRevisionDeletion
   Description: Method to validate the possibility of Course revision deletion.
   OperationID: ValidateCourseRevisionDeletion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCourseRevisionDeletion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCourseRevisionDeletion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourseRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourseRevision
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCourseRevisionAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCourseRevisionAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseRevisionAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseRevisionAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseRevisionAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CourseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseRevisionAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseRevisionAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseRevisionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseRevisionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CourseRow] = obj["value"]
      pass

class Erp_Tablesets_CourseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The user defined training course ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Training Course.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseRevisionAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
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

class Erp_Tablesets_CourseRevisionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The user defined training course revision code.  """  
      self.Description:str = obj["Description"]
      """  The description of the training course revision.  """  
      self.RevDate:str = obj["RevDate"]
      """  The date that the revision was created. When a new revision is created this will default to the current date.  """  
      self.EffDate:str = obj["EffDate"]
      """  The date that the training course revision will become effective. When a new revision is created this will default to the current date.  """  
      self.Duration:int = obj["Duration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.DurationType:str = obj["DurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.ExpiresIn:int = obj["ExpiresIn"]
      """  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  """  
      self.ExpirationType:str = obj["ExpirationType"]
      """  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  """  
      self.Syllabus:str = obj["Syllabus"]
      """  The free-format details of the syllabus for the course.  """  
      self.Prerequisites:str = obj["Prerequisites"]
      """  The free-format details of the prerequisites of the course.  """  
      self.Materials:str = obj["Materials"]
      """  The free-format details of the course materials.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The user defined training course ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Training Course.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   courseID
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateCourse_input:
   """ Required : 
   sourceCourseID
   sourceRevCode
   newCourseID
   newCourseDesc
   newRevCode
   newRevDesc
   ds
   """  
   def __init__(self, obj):
      self.sourceCourseID:str = obj["sourceCourseID"]
      self.sourceRevCode:str = obj["sourceRevCode"]
      self.newCourseID:str = obj["newCourseID"]
      self.newCourseDesc:str = obj["newCourseDesc"]
      self.newRevCode:str = obj["newRevCode"]
      self.newRevDesc:str = obj["newRevDesc"]
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

class DuplicateCourse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CourseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The user defined training course ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Training Course.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseListTableset:
   def __init__(self, obj):
      self.CourseList:list[Erp_Tablesets_CourseListRow] = obj["CourseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CourseRevisionAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CourseID:str = obj["CourseID"]
      self.RevisionCode:str = obj["RevisionCode"]
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

class Erp_Tablesets_CourseRevisionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The Training Course ID.  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  The user defined training course revision code.  """  
      self.Description:str = obj["Description"]
      """  The description of the training course revision.  """  
      self.RevDate:str = obj["RevDate"]
      """  The date that the revision was created. When a new revision is created this will default to the current date.  """  
      self.EffDate:str = obj["EffDate"]
      """  The date that the training course revision will become effective. When a new revision is created this will default to the current date.  """  
      self.Duration:int = obj["Duration"]
      """  The duration of the course. When a new revision is created this will default to 1.  """  
      self.DurationType:str = obj["DurationType"]
      """  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  """  
      self.ExpiresIn:int = obj["ExpiresIn"]
      """  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  """  
      self.ExpirationType:str = obj["ExpirationType"]
      """  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  """  
      self.Syllabus:str = obj["Syllabus"]
      """  The free-format details of the syllabus for the course.  """  
      self.Prerequisites:str = obj["Prerequisites"]
      """  The free-format details of the prerequisites of the course.  """  
      self.Materials:str = obj["Materials"]
      """  The free-format details of the course materials.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CourseID:str = obj["CourseID"]
      """  The user defined training course ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Training Course.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CourseTableset:
   def __init__(self, obj):
      self.Course:list[Erp_Tablesets_CourseRow] = obj["Course"]
      self.CourseRevision:list[Erp_Tablesets_CourseRevisionRow] = obj["CourseRevision"]
      self.CourseRevisionAttch:list[Erp_Tablesets_CourseRevisionAttchRow] = obj["CourseRevisionAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCourseTableset:
   def __init__(self, obj):
      self.Course:list[Erp_Tablesets_CourseRow] = obj["Course"]
      self.CourseRevision:list[Erp_Tablesets_CourseRevisionRow] = obj["CourseRevision"]
      self.CourseRevisionAttch:list[Erp_Tablesets_CourseRevisionAttchRow] = obj["CourseRevisionAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   courseID
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CourseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CourseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CourseTableset] = obj["returnObj"]
      pass

class GetCourseDurationTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCourseExpirationTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_CourseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCourseRevisionAttch_input:
   """ Required : 
   ds
   courseID
   revisionCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      self.courseID:str = obj["courseID"]
      self.revisionCode:str = obj["revisionCode"]
      pass

class GetNewCourseRevisionAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCourseRevision_input:
   """ Required : 
   ds
   courseID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      self.courseID:str = obj["courseID"]
      pass

class GetNewCourseRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCourse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

class GetNewCourse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCourse
   whereClauseCourseRevision
   whereClauseCourseRevisionAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCourse:str = obj["whereClauseCourse"]
      self.whereClauseCourseRevision:str = obj["whereClauseCourseRevision"]
      self.whereClauseCourseRevisionAttch:str = obj["whereClauseCourseRevisionAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CourseTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCourseTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCourseTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CourseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCourseDeletion_input:
   """ Required : 
   CourseID
   """  
   def __init__(self, obj):
      self.CourseID:str = obj["CourseID"]
      """  Course ID  """  
      pass

class ValidateCourseDeletion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isDeleteOK:bool = obj["isDeleteOK"]
      pass

      """  output parameters  """  

class ValidateCourseID_input:
   """ Required : 
   courseID
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      """  Course ID  """  
      pass

class ValidateCourseID_output:
   def __init__(self, obj):
      pass

class ValidateCourseRevisionDeletion_input:
   """ Required : 
   CourseID
   RevisionCode
   """  
   def __init__(self, obj):
      self.CourseID:str = obj["CourseID"]
      """  Course ID  """  
      self.RevisionCode:str = obj["RevisionCode"]
      """  Course Revision Code  """  
      pass

class ValidateCourseRevisionDeletion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isDeleteOK:bool = obj["isDeleteOK"]
      pass

      """  output parameters  """  

class ValidateCourseRevision_input:
   """ Required : 
   courseID
   revisionCode
   """  
   def __init__(self, obj):
      self.courseID:str = obj["courseID"]
      """  Course ID  """  
      self.revisionCode:str = obj["revisionCode"]
      """  Revision Code  """  
      pass

class ValidateCourseRevision_output:
   def __init__(self, obj):
      pass

